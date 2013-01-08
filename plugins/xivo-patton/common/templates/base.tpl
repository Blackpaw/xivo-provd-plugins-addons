cli version 3.20
timer check_config now + 1 minute "provisioning execute PF_PROVISIONING_CONFIG"
timer check_firmware now + 1 minute "provisioning execute PF_PROVISIONING_FIRMWARE"

{% if ntp_enabled -%}
sntp-client
sntp-client server primary {{ ntp_ip }} port 123 version 4
{% endif -%}

{{ XX_timezone }}

{% if admin_password -%}
{% if admin_username -%}
administrator {{ admin_username }} password {{ admin_password }}
{% endif -%}
{% endif -%}

{% if user_password -%}
{% if user_username -%}
operator {{ user_username }} password {{ user_password }}
{% endif -%}
{% endif -%}

system

  ic voice 0
    low-bitrate-codec g729

profile ppp default

profile tone-set default

profile voip default
  codec 1 g711alaw64k rx-length 20 tx-length 20
  codec 2 g711ulaw64k rx-length 20 tx-length 20
  {% if  sip_lines['1'].XX_dtmf_inband_transfer -%}
    dtmf-relay {{ sip_lines['1'].XX_dtmf_inband_transfer }}
  {% endif -%}


profile pstn default

profile ringing-cadence default
  play 1 1000
  pause 2 4000

profile sip default
  no autonomous-transitioning

profile aaa default
  method 1 local
  method 2 none

profile provisioning PF_PROVISIONING_CONFIG
  destination configuration
  location 1 $(dhcp.66)/$(system.mac).cfg
  activation reload graceful


profile provisioning PF_PROVISIONING_FIRMWARE
  destination script
  location 1 $(dhcp.66)/firmware/bw
  action reload graceful


context ip router

  interface eth0
    ipaddress dhcp
    tcp adjust-mss rx mtu
    tcp adjust-mss tx mtu

context cs switch
  national-prefix 0
  international-prefix 00

  routing-table called-uri RT_FROM_XIVO
  {% for line in sip_lines.itervalues() %}

    route sip:{{ line['auth_username'] }}@.% dest-interface IF_FXS_0{{ line['XX_line_no'] -1 }}

  {% endfor -%}

{% for line in sip_lines.itervalues() %}
   routing-table called-e164 RT_FROM_FXS_0{{ line['XX_line_no'] -1 }}
    route .T dest-interface IF_SIP_XIVO MAP_EXTEN_TO_USER
{% endfor -%}

  mapping-table calling-e164 to calling-e164 MAP_EXTEN_TO_USER

  {% for line in sip_lines.itervalues() %}

    map {{ line['number']}} to {{ line['auth_username'] }}

  {% endfor -%}


  interface sip IF_SIP_XIVO
    bind context sip-gateway SIP_GW
    route call dest-table RT_FROM_XIVO
    remote {{ sip_lines['1'].proxy_ip }}

  {% for line in sip_lines.itervalues() %}

    interface fxs IF_FXS_0{{ line['XX_line_no'] -1 }}
      route call dest-table RT_FROM_FXS_0{{ line['XX_line_no'] -1 }}
      caller-id-presentation pre-ring
      subscriber-number {{ line['number']}}

  {% endfor -%}

  context cs switch

  no shutdown

authentication-service AUTH_SERV

  {% for line in sip_lines.itervalues() %}

    username {{ line['auth_username'] }} password {{ line['password'] }}

  {% endfor -%}

location-service LOC_SERV
  domain 1 {{ sip_lines['1'].proxy_ip }}

  identity-group XIVO
    registration outbound
      registrar {{ sip_lines['1'].proxy_ip }}
      lifetime 60
      register auto
      retry-timeout on-system-error 10
      retry-timeout on-client-error 10
      retry-timeout on-server-error 10

    message inbound
      message-server {{ sip_lines['1'].proxy_ip }}
      lifetime 60
      subscribe implicit
      retry-timeout on-system-error 10
      retry-timeout on-client-error 10
      retry-timeout on-server-error 10

  {% for line in sip_lines.itervalues() %}

    identity {{ line['auth_username'] }} inherits XIVO

    authentication outbound
      authenticate 1 authentication-service AUTH_SERV username {{ line['auth_username'] }}

  {% endfor -%}

context sip-gateway SIP_GW

  interface IF_GW_SIP
    bind interface eth0 context router port 5060

context sip-gateway SIP_GW
  bind location-service LOC_SERV
  no shutdown

port ethernet 0 0
  medium auto
  encapsulation ip
{% if vlan_enabled -%}
  vlan {{ vlan_id }}
    bind interface eth0 router
    encapsulation ip
    no shutdown
{% else -%}
  bind interface eth0 router
  no shutdown
{% endif -%}

port ethernet 0 0
no shutdown




  {% for line in sip_lines.itervalues() %}

    port fxs 0 {{ line['XX_line_no'] -1 }}
      encapsulation cc-fxs
      bind interface IF_FXS_0{{ line['XX_line_no'] -1 }} switch
    no shutdown

  {% endfor -%}
