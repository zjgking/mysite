import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class FWtable(models.Model):
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

class SWtable(models.Model):
    url = models.URLField(max_length=200)
    vendors = models.CharField(max_length=20) # 厂商
    cpxh = models.CharField(max_length=30)  #产品型号
    ywcw = models.IntegerField()    #业务插槽数量
    jhwb = models.IntegerField()    #交换网板数量
    zkb = models.IntegerField()     #主控板数量
    dy = models.IntegerField()      #电源数量
    fs = models.IntegerField()#风扇
    poe = models.CharField(max_length=2) #是否支持poe供电

    rj45 = models.IntegerField()  #千兆接口数量
    sfp = models.IntegerField()  #千兆光接口数量
    sfpp = models.IntegerField()  #万兆光口
    sfppc = models.IntegerField()  #万兆电口
    g25 = models.IntegerField()  #25GE接口
    g40 = models.IntegerField()  #40GE接口
    g100 = models.IntegerField()  #100GE接口
    fcdk = models.IntegerField()   #FC 存储接口数量

    dk = models.FloatField()  #交换背板容量
    v4zfl = models.FloatField()  #IPv4数据包率
    v6zfl = models.FloatField()  #IPv6转发率
    macsl =models.IntegerField() #MAC地址数量
    arpsl = models.IntegerField() #ARP数量
    stacks = models.CharField(max_length=2)  #支持的堆叠数量

    Notes =models.CharField(max_length=200, blank=True)

class swtable(models.Model):
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vendors = models.CharField(db_column='Vendors', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mod = models.CharField(db_column='MOD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    io_slots = models.IntegerField(db_column='I/O_Slots')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    switch_fabric = models.IntegerField(db_column='Switch_Fabric')  # Field name made lowercase.
    redu_switch_fabric = models.CharField(db_column='Redu_Switch_Fabric', max_length=5, blank=True, null=True)  # Field name made lowercase.
    routing_engine = models.IntegerField(db_column='Routing_Engine')  # Field name made lowercase.
    power_supplies = models.IntegerField(db_column='Power_Supplies')  # Field name made lowercase.
    fans = models.IntegerField(db_column='Fans')  # Field name made lowercase.
    cpu = models.CharField(db_column='CPU', max_length=25, blank=True, null=True)  # Field name made lowercase.
    memory = models.IntegerField(db_column='Memory')  # Field name made lowercase.
    hard_disk = models.CharField(db_column='Hard_Disk', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mgmt = models.IntegerField(db_column='MGMT')  # Field name made lowercase.
    usb_port = models.IntegerField(db_column='USB_Port')  # Field name made lowercase.
    poe = models.CharField(db_column='POE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    rackunit = models.IntegerField(db_column='Rack_Unit_')  # Field name made lowercase. Field renamed because it ended with '_'.
    sfp_port_combo = models.IntegerField(db_column='SFP_Port_Combo')  # Field name made lowercase.
    ge_port_combo = models.IntegerField(db_column='GE_Port_Combo')  # Field name made lowercase.
    ge_port_chasis = models.IntegerField(db_column='GE_Port_Chasis')  # Field name made lowercase.
    sfp_port_chasis = models.IntegerField(db_column='SFP_Port_Chasis')  # Field name made lowercase.
    sfpp_port_chasis = models.IntegerField(db_column='SFP+_Port_Chasis')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    g10_port_chasis = models.IntegerField(db_column='10GE_Port_Chasis')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ge_g10_adapt = models.IntegerField(db_column='GE_10GE_Port_Adapt')  # Field name made lowercase.
    g25_port = models.CharField(db_column='25GE_Port', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    g40_port = models.IntegerField(db_column='40GE_Port')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    g100_port = models.IntegerField(db_column='100GE_Port')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    fc_port = models.CharField(db_column='FC-Port', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    max_ge_port = models.CharField(db_column='Max_GE_Port', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_sfp_port = models.CharField(db_column='Max_SFP_Port', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_10g_port = models.IntegerField(db_column='Max_10GE_Port')  # Field name made lowercase.
    max_sfpp_port = models.IntegerField(db_column='Max_SFP+_Port')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    max_25g_port = models.CharField(db_column='Max_24GE_Port', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_40g_port = models.IntegerField(db_column='Max_40GE_Port')  # Field name made lowercase.
    max_100g_port = models.IntegerField(db_column='Max_100GE_Port')  # Field name made lowercase.
    switching_capacity = models.CharField(db_column='Switching_Capacity', max_length=5, blank=True, null=True)  # Field name made lowercase.
    forwarding_capacity = models.CharField(db_column='Forwarding_Capacity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipv4_forwarding_performance_pps = models.CharField(db_column='IPv4_Forwarding_performance_pps', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ipv6_forwarding_performance_pps = models.CharField(db_column='IPv6_Forwarding_performance_pps', max_length=255, blank=True, null=True)  # Field name made lowercase.
    l2_forwarding_performance_pps = models.CharField(db_column='L2_Forwarding_performance_pps', max_length=255, blank=True, null=True)  # Field name made lowercase.
    perslots_forwarding_performance_pps = models.CharField(db_column='PerSlots_Forwarding_performance_pps', max_length=12, blank=True, null=True)  # Field name made lowercase.
    interslot_capacity_pps = models.CharField(db_column='Inter-slot_switching_capacity_pps', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ipv4_route_entries = models.CharField(db_column='IPv4_Route_Entries', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ipv6_route_entries = models.CharField(db_column='IPv6_Route_Entries', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fib_ipv4 = models.CharField(db_column='FIB_IPv4', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fip_ipv6 = models.CharField(db_column='FIP_IPv6', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ecmp = models.IntegerField(db_column='ECMP')  # Field name made lowercase.
    mac = models.CharField(db_column='MAC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    arp = models.CharField(db_column='ARP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vlan = models.CharField(db_column='VLAN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    stp_instance = models.CharField(db_column='STP_Instance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jumbo_frame = models.IntegerField(db_column='Jumbo_Frame')  # Field name made lowercase.
    g10_cache = models.CharField(db_column='10GE_Cache', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    ge_cache = models.CharField(db_column='GE_Cache', max_length=5, blank=True, null=True)  # Field name made lowercase.
    base_system = models.CharField(db_column='Base_System', max_length=255, blank=True, null=True)  # Field name made lowercase.
    expansion_module = models.CharField(db_column='Expansion_Module', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gemodule = models.CharField(db_column='GE-Module', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g10module = models.CharField(db_column='10GE-Module', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    g25module = models.CharField(db_column='25GE-Module', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    g40module = models.CharField(db_column='40GE-Module', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    g100module = models.CharField(db_column='100GE-Module', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    mserver_module = models.CharField(db_column='Multi-Server-Module', max_length=5, blank=True, null=True)  # 多服务板块模块，Field name made lowercase. Field renamed to remove unsuitable characters.
    poe_features = models.CharField(db_column='POE_Features', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdn = models.CharField(db_column='SDN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    openflow = models.CharField(db_column='Openflow', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ztp = models.CharField(db_column='ZTP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    rollback = models.CharField(db_column='Rollback', max_length=5, blank=True, null=True)  # Field name made lowercase.
    evpn = models.CharField(db_column='EVPN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gres = models.CharField(db_column='GRES', max_length=5, blank=True, null=True)  # Field name made lowercase.
    svi_irb = models.CharField(db_column='SVI_IRB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    stacks_type = models.CharField(db_column='Stacks_Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mchass_lag = models.CharField(db_column='Multi-Chass-LAG', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stacknumber = models.IntegerField(db_column='Number_Stackable_')  # Field name made lowercase. Field renamed because it ended with '_'.
    stacksport_num = models.CharField(db_column='StacksPort_Num', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stacksport_type = models.CharField(db_column='StacksPort_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vsys = models.CharField(db_column='Virtual_System', max_length=12, blank=True, null=True)  # Field name made lowercase.
    evi_otv_evn = models.CharField(db_column='EVI_OTV_EVN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vrf_lite_scalability = models.CharField(db_column='VRF_Lite_Scalability', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vrouters = models.CharField(db_column='vRouters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vswitchs = models.CharField(db_column='vSwitchs', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pfc = models.CharField(db_column='PFC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ets = models.CharField(db_column='ETS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dcbx = models.CharField(db_column='DCBX', max_length=5, blank=True, null=True)  # Field name made lowercase.
    qbb = models.CharField(db_column='802.1Qbb', max_length=5, blank=True, null=True)  # 802.1Qbb。Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    qaz = models.CharField(db_column='802.1Qaz', max_length=5, blank=True, null=True)  # 802.1Qaz 。Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    qau = models.CharField(db_column='802.1Qau', max_length=255, blank=True, null=True)  # 802.1Qau。Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    evb = models.CharField(db_column='EVB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fcoe = models.CharField(db_column='FCoE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    trill = models.CharField(db_column='TRILL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ovsdb = models.CharField(db_column='OVSDB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vxlan = models.CharField(db_column='Vxlan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vxlanl2_gateway = models.CharField(db_column='VxlanL2_Gateway', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vxlanl3_gateway = models.CharField(db_column='VxlanL3-Gateway', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    power_nominal_rating = models.IntegerField(db_column='Power_Nominal_Rating')  # Field name made lowercase.
    power_max_rating = models.IntegerField(db_column='Power_Max_Rating')  # Field name made lowercase.
    operating_temperature = models.CharField(db_column='Operating_Temperature', max_length=255, blank=True, null=True)  # Field name made lowercase.
    relative_humidity = models.CharField(db_column='Relative_Humidity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airflow = models.CharField(db_column='Airflow', max_length=25, blank=True, null=True)  # Field name made lowercase.
    t1 = models.CharField(db_column='T1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t2 = models.CharField(db_column='T2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t3 = models.CharField(db_column='T3', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ospf = models.CharField(db_column='OSPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isis = models.CharField(db_column='IS-IS', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bgp = models.CharField(db_column='BGP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mpls = models.CharField(db_column='MPLS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mplsl2vpn = models.IntegerField(db_column='MPLS_L2VPN_Num')  # Field name made lowercase.
    mplsl3vpn = models.IntegerField(db_column='MPLS_L3VPN_Num')  # Field name made lowercase.
    vpls_num = models.IntegerField(db_column='VPLS_Num')  # Field name made lowercase.
    gre_num = models.IntegerField(db_column='GRE_Tunnels_Num')  # Field name made lowercase.
    pbr_fbr = models.CharField(db_column='PBR_FBR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    t5 = models.CharField(db_column='T5', max_length=12, blank=True, null=True)  # Field name made lowercase.
    stp = models.CharField(db_column='STP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dhcp = models.CharField(db_column='DHCP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t6 = models.CharField(db_column='T6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t7 = models.CharField(db_column='T7', max_length=25, blank=True, null=True)  # Field name made lowercase.
    l3_interface = models.CharField(db_column='L3_Interface', max_length=25, blank=True, null=True)  # Field name made lowercase.
    t9 = models.CharField(db_column='T9', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t10 = models.CharField(db_column='T10', max_length=12, blank=True, null=True)  # Field name made lowercase.
    t11 = models.CharField(db_column='T11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t12 = models.CharField(db_column='T12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipv6_tunnel_type = models.CharField(db_column='IPv6_Tunnel_Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ipv6_security = models.CharField(db_column='IPv6_Security', max_length=25, blank=True, null=True)  # Field name made lowercase.
    t14 = models.CharField(db_column='T14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bfd = models.CharField(db_column='BFD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mtbf = models.CharField(db_column='MTBF', max_length=25, blank=True, null=True)  # Field name made lowercase.
    graceful_routing_switchove = models.CharField(db_column='Graceful_Routing_Switchove', max_length=25, blank=True, null=True)  # Field name made lowercase.
    oam = models.CharField(db_column='OAM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_rr = models.CharField(db_column='IP_RR', max_length=45, blank=True, null=True)  # Field name made lowercase.
    frr = models.CharField(db_column='FRR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    t18 = models.CharField(db_column='T18', max_length=45, blank=True, null=True)  # Field name made lowercase.
    t19 = models.CharField(db_column='T19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t20 = models.CharField(db_column='T20', max_length=255, blank=True, null=True)  # Field name made lowercase.
    multicast_type = models.CharField(db_column='Multicast_Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    igmp_groups = models.CharField(db_column='IGMP_Groups', max_length=45, blank=True, null=True)  # Field name made lowercase.
    v4_multicast = models.CharField(db_column='IPv4-Multicast_Routes', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    v6_multicast = models.CharField(db_column='IPv6-Multicast_Routes', max_length=5, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dhcp_snooping = models.CharField(db_column='DHCP_Snooping', max_length=45, blank=True, null=True)  # Field name made lowercase.
    qos_type = models.CharField(db_column='QoS_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    per_port_queues = models.IntegerField(db_column='Per_Port_Queues')  # Field name made lowercase.
    t21 = models.CharField(db_column='T21', max_length=12, blank=True, null=True)  # Field name made lowercase.
    t22 = models.CharField(db_column='T22', max_length=45, blank=True, null=True)  # Field name made lowercase.
    t23 = models.CharField(db_column='T23', max_length=12, blank=True, null=True)  # Field name made lowercase.
    t24 = models.CharField(db_column='T24', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpu_queues = models.CharField(db_column='CPU-Queues', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    qos_rate_limiters = models.CharField(db_column='QoS_Rate_Limiters', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qos_entries = models.CharField(db_column='QoS_Entries_', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    t25 = models.CharField(db_column='T25', max_length=255, blank=True, null=True)  # Field name made lowercase.
    port_security = models.CharField(db_column='Port_Security', max_length=45, blank=True, null=True)  # Field name made lowercase.
    x8021 = models.CharField(db_column='802.1x', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    acl_entries = models.CharField(db_column='ACL_Entries', max_length=5, blank=True, null=True)  # Field name made lowercase.
    urpf = models.CharField(db_column='uRPF', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cpu_dos_protection = models.CharField(db_column='CPU_rate_limiters_DoS-protection', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pvlan_mux = models.CharField(db_column='Pvlan_MUX', max_length=12, blank=True, null=True)  # Field name made lowercase.
    storm_control = models.CharField(db_column='Storm_Control', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arp_inspection = models.CharField(db_column='ARP_Inspection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bpdu_guard = models.CharField(db_column='BPDU_Guard', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dhcp_security = models.CharField(db_column='DHCP_Security', max_length=255, blank=True, null=True)  # Field name made lowercase.
    netflow_netstream_cflow = models.CharField(db_column='Netflow_NetStream_cFlow', max_length=12, blank=True, null=True)  # Field name made lowercase.
    netflow_entries = models.CharField(db_column='Netflow_Entries', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sflow = models.CharField(db_column='sFlow', max_length=5, blank=True, null=True)  # Field name made lowercase.
    management_style = models.CharField(db_column='Management_Style', max_length=255, blank=True, null=True)  # Field name made lowercase.
    span_rspan = models.CharField(db_column='SPAN_RSPAN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    erspan = models.CharField(db_column='ERSPAN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cdp_lldp = models.CharField(db_column='CDP_LLDP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    api = models.CharField(db_column='API', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clocks = models.CharField(db_column='Clocks', max_length=255, blank=True, null=True)  # Field name made lowercase.
    az8023 = models.CharField(db_column='802.3az', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    sla_rpm = models.CharField(db_column='SLA_RPM', max_length=45, blank=True, null=True)  # Field name made lowercase.

