import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class fw(models.Model):
    URL = models.URLField(max_length=150)
    Vendors = models.CharField(max_length=20)
    Model = models.CharField(max_length=30)
    Throughput = models.FloatField()
    Concurrent_Sessions = models.FloatField()
    New_Sessions_Sec = models.IntegerField()
    GE_RJ45 = models.IntegerField()
    GE_SFP =  models.IntegerField()
    Cop_10GE = models.IntegerField()
    SFPP_10GE = models.IntegerField()
    QSFPP_40GE = models.IntegerField()
    CFP2_QSFP28_100GE = models.IntegerField()
    Interface_Module_Slots = models.IntegerField()
    Power = models.IntegerField()
    Processor_Module_Slots = models.IntegerField()
    Throughput_PpSec = models.FloatField()
    Local_Storage = models.IntegerField()
    Notes =models.CharField(max_length=200, blank=True)
    Created_times = models.DateTimeField(auto_now_add = True)
    Update_times = models.DateTimeField(auto_now = True)
    Operater = models.CharField(max_length=10)

    #def __str__(self):
    #   return self.Vendors,self.Notes

class sw(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    vendors = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    mod = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    io_slots = models.IntegerField()  # Field name made lowercase. Field renamed to remove unsuitable characters.
    switch_fabric = models.IntegerField()  # Field name made lowercase.
    redu_switch_fabric = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    routing_engine = models.IntegerField()  # Field name made lowercase.
    power_supplies = models.IntegerField()  # Field name made lowercase.
    fans = models.IntegerField()  # Field name made lowercase.
    cpu = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    memory = models.IntegerField()  # Field name made lowercase.
    hard_disk = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase.
    mgmt = models.IntegerField()  # Field name made lowercase.
    usb_port = models.IntegerField()  # Field name made lowercase.
    poe = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    rackunit = models.IntegerField()  # Field name made lowercase. Field renamed because it ended with '_'.
    sfp_port_combo = models.IntegerField()  # Field name made lowercase.
    ge_port_combo = models.IntegerField()  # Field name made lowercase.
    ge_port_chasis = models.IntegerField()  # Field name made lowercase.
    sfp_port_chasis = models.IntegerField()  # Field name made lowercase.
    sfpp_port_chasis = models.IntegerField()  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    g10_port_chasis = models.IntegerField()  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ge_g10_adapt = models.IntegerField()  # Field name made lowercase.
    g25_port = models.IntegerField()  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    g40_port = models.IntegerField()  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    g100_port = models.IntegerField()  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    fc_port = models.IntegerField()  # Field name made lowercase. Field renamed to remove unsuitable characters.
    max_ge_port = models.IntegerField()  # Field name made lowercase.
    max_sfp_port = models.IntegerField()  # Field name made lowercase.
    max_10g_port = models.IntegerField()  # Field name made lowercase.
    max_sfpp_port = models.IntegerField()  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    max_25g_port = models.IntegerField()  # Field name made lowercase.
    max_40g_port = models.IntegerField()  # Field name made lowercase.
    max_100g_port = models.IntegerField()  # Field name made lowercase.
    switching_capacity = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    forwarding_capacity = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipv4_forwarding_performance_pps = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    ipv6_forwarding_performance_pps = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    l2_forwarding_performance_pps = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    perslots_forwarding_performance_pps = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    interslot_capacity_pps = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ipv4_route_entries = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    ipv6_route_entries = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    fib_ipv4 = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    fip_ipv6 = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    ecmp = models.IntegerField()  # Field name made lowercase.
    mac = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    arp = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    vlan = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    stp_instance = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    jumbo_frame = models.IntegerField()  # Field name made lowercase.
    g10_cache = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ge_cache = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    base_system = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    expansion_module = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    gemodule = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g10module = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    g25module = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    g40module = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    g100module = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    mserver_module = models.CharField( max_length=5, blank=True, null=True)  # 多服务板块模块，Field name made lowercase. Field renamed to remove unsuitable characters.
    poe_features = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdn = models.CharField( max_length=45, blank=True, null=True)  # Field name made lowercase.
    openflow = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    ztp = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    rollback = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    evpn = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    gres = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    svi_irb = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    stacks_type = models.CharField( max_length=45, blank=True, null=True)  # Field name made lowercase.
    mchass_lag = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stacknumber = models.IntegerField()  # Field name made lowercase. Field renamed because it ended with '_'.
    stacksport_num = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    stacksport_type = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    vsys = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase.
    evi_otv_evn = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    vrf_lite_scalability = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    vrouters = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    vswitchs = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    pfc = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    ets = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    dcbx = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    qbb = models.CharField(max_length=5, blank=True, null=True)  # 802.1Qbb。Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    qaz = models.CharField(max_length=5, blank=True, null=True)  # 802.1Qaz 。Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    qau = models.CharField(max_length=255, blank=True, null=True)  # 802.1Qau。Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    evb = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    fcoe = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    trill = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ovsdb = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    vxlan = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    vxlanl2_gateway = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    vxlanl3_gateway = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    power_nominal_rating = models.IntegerField()  # Field name made lowercase.
    power_max_rating = models.IntegerField()  # Field name made lowercase.
    operating_temperature = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    relative_humidity = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    airflow = models.CharField( max_length=25, blank=True, null=True)  # Field name made lowercase.
    t1 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    ospf = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    isis = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bgp = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    mpls = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    mplsl2vpn = models.IntegerField()  # Field name made lowercase.
    mplsl3vpn = models.IntegerField()  # Field name made lowercase.
    vpls_num = models.IntegerField()  # Field name made lowercase.
    gre_num = models.IntegerField()  # Field name made lowercase.
    pbr_fbr = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    stp = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    dhcp = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    l3_interface = models.CharField( max_length=25, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipv6_tunnel_type = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    ipv6_security = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    bfd = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    mtbf = models.CharField( max_length=25, blank=True, null=True)  # Field name made lowercase.
    graceful_routing_switchove = models.CharField( max_length=25, blank=True, null=True)  # Field name made lowercase.
    oam = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_rr = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    frr = models.CharField( max_length=25, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    multicast_type = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    igmp_groups = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    v4_multicast = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    v6_multicast = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dhcp_snooping = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    qos_type = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    per_port_queues = models.IntegerField()  # Field name made lowercase.
    t21 = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpu_queues = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qos_rate_limiters = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    qos_entries = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    t25 = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    port_security = models.CharField( max_length=45, blank=True, null=True)  # Field name made lowercase.
    x8021 = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    acl_entries = models.CharField(max_length=5, blank=True, null=True)  # Field name made lowercase.
    urpf = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    cpu_dos_protection = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pvlan_mux = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase.
    storm_control = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    arp_inspection = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    bpdu_guard = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    dhcp_security = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    netflow_netstream_cflow = models.CharField( max_length=12, blank=True, null=True)  # Field name made lowercase.
    netflow_entries = models.CharField(max_length=12, blank=True, null=True)  # Field name made lowercase.
    sflow = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    management_style = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    span_rspan = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    erspan = models.CharField( max_length=5, blank=True, null=True)  # Field name made lowercase.
    cdp_lldp = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    api = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    clocks = models.CharField( max_length=255, blank=True, null=True)  # Field name made lowercase.
    az8023 = models.CharField(max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    sla_rpm = models.CharField(max_length=45, blank=True, null=True)  # Field name made lowercase.

