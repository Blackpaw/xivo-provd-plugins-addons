<<VOIP CONFIG FILE>>Version:2.0002

<SIP CONFIG MODULE>
SIP  Port          :5060
--SIP Line List--  :
{% for line_no, line in sip_lines.iteritems() %}
SIP1 Phone Number  :{{ line_no|int - 1 }}
SIP1 Display Name  :{{ line['displayname'] }}
SIP1 Sip Name      :{{ line['displayname'] }}
SIP1 Register Addr :{{ line['proxy_ip'] }}
SIP1 Register Port :{{ line['proxy_port']|d(5060) }}
SIP1 Register User :{{ line['username'] }}
SIP1 Register Pswd :{{ line['password'] }}
SIP1 Register TTL  :60
SIP1 Enable Reg    :1
SIP1 Proxy Addr    :{{ line['proxy_ip'] }}
SIP1 Proxy Port    :{{ line['proxy_port']|d(5060) }}
SIP1 Proxy User    :{{ line['username'] }}
SIP1 Proxy Pswd    :{{ line['password'] }}

{% if line['backup_proxy_ip'] -%}
SIP1 BakProxy Addr :{{ line['backup_proxy_ip'] }}
SIP1 BakProxy Port :{{ line['backup_proxy_port']|d(5060) }}
{% endif %}

{% endfor %}

<<END OF FILE>>

