<?xml version="1.0" encoding="UTF-8" ?>
<gs_provision version="1">
 <config version="1">
{# SIP per-line settings -#}
{% for line_no, line in sip_lines.iteritems() %}
  <P271>1</P271>
  <P270>{{ line['auth_username'] }}</P270>
  <P47>{{ line['registrar_ip'] }}</P47>
  <P2312>{{ line['backup_registrar_ip'] }}</P2312>
  <P48>{{ line['proxy_ip'] }}</P48>
  <P35>{{ line['auth_username'] }}</P35>
  <P36>{{ line['auth_username'] }}</P36>
  <P34>{{ line['password'] }}</P34>
  <P3>{{ line['display_name'] }}</P3>
{% endfor -%}
 </config>
</gs_provision>

