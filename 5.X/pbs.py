# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pbs', [dirname(__file__)])
        except ImportError:
            import _pbs
            return _pbs
        if fp is not None:
            try:
                _mod = imp.load_module('_pbs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pbs = swig_import_helper()
    del swig_import_helper
else:
    import _pbs
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def new_attrl(*args):
  return _pbs.new_attrl(*args)
new_attrl = _pbs.new_attrl

def new_attropl(*args):
  return _pbs.new_attropl(*args)
new_attropl = _pbs.new_attropl

def new_batch_status():
  return _pbs.new_batch_status()
new_batch_status = _pbs.new_batch_status

def get_error():
  return _pbs.get_error()
get_error = _pbs.get_error
class attrlArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, attrlArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, attrlArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pbs.new_attrlArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pbs.delete_attrlArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _pbs.attrlArray___getitem__(self, *args)
    def __setitem__(self, *args): return _pbs.attrlArray___setitem__(self, *args)
    def cast(self): return _pbs.attrlArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _pbs.attrlArray_frompointer
    if _newclass:frompointer = staticmethod(_pbs.attrlArray_frompointer)
attrlArray_swigregister = _pbs.attrlArray_swigregister
attrlArray_swigregister(attrlArray)

def attrlArray_frompointer(*args):
  return _pbs.attrlArray_frompointer(*args)
attrlArray_frompointer = _pbs.attrlArray_frompointer

ATTR_a = _pbs.ATTR_a
ATTR_c = _pbs.ATTR_c
ATTR_e = _pbs.ATTR_e
ATTR_f = _pbs.ATTR_f
ATTR_g = _pbs.ATTR_g
ATTR_h = _pbs.ATTR_h
ATTR_j = _pbs.ATTR_j
ATTR_k = _pbs.ATTR_k
ATTR_l = _pbs.ATTR_l
ATTR_m = _pbs.ATTR_m
ATTR_o = _pbs.ATTR_o
ATTR_p = _pbs.ATTR_p
ATTR_q = _pbs.ATTR_q
ATTR_r = _pbs.ATTR_r
ATTR_t = _pbs.ATTR_t
ATTR_array_id = _pbs.ATTR_array_id
ATTR_u = _pbs.ATTR_u
ATTR_v = _pbs.ATTR_v
ATTR_A = _pbs.ATTR_A
ATTR_args = _pbs.ATTR_args
ATTR_reservation_id = _pbs.ATTR_reservation_id
ATTR_login_node_id = _pbs.ATTR_login_node_id
ATTR_login_prop = _pbs.ATTR_login_prop
ATTR_external_nodes = _pbs.ATTR_external_nodes
ATTR_multi_req_alps = _pbs.ATTR_multi_req_alps
ATTR_M = _pbs.ATTR_M
ATTR_N = _pbs.ATTR_N
ATTR_S = _pbs.ATTR_S
ATTR_depend = _pbs.ATTR_depend
ATTR_inter = _pbs.ATTR_inter
ATTR_stagein = _pbs.ATTR_stagein
ATTR_stageout = _pbs.ATTR_stageout
ATTR_jobtype = _pbs.ATTR_jobtype
ATTR_submit_host = _pbs.ATTR_submit_host
ATTR_init_work_dir = _pbs.ATTR_init_work_dir
ATTR_pbs_o_initdir = _pbs.ATTR_pbs_o_initdir
ATTR_pbs_o_rootdir = _pbs.ATTR_pbs_o_rootdir
ATTR_pbs_o_workdir = _pbs.ATTR_pbs_o_workdir
ATTR_pbs_o_host = _pbs.ATTR_pbs_o_host
ATTR_pbs_o_server = _pbs.ATTR_pbs_o_server
ATTR_pbs_o_home = _pbs.ATTR_pbs_o_home
ATTR_pbs_o_logname = _pbs.ATTR_pbs_o_logname
ATTR_pbs_o_path = _pbs.ATTR_pbs_o_path
ATTR_pbs_o_mail = _pbs.ATTR_pbs_o_mail
ATTR_pbs_o_shell = _pbs.ATTR_pbs_o_shell
ATTR_pbs_o_tz = _pbs.ATTR_pbs_o_tz
ATTR_pbs_o_lang = _pbs.ATTR_pbs_o_lang
ATTR_pbs_o_uid = _pbs.ATTR_pbs_o_uid
ATTR_pbs_o_submit_filter = _pbs.ATTR_pbs_o_submit_filter
ATTR_ctime = _pbs.ATTR_ctime
ATTR_exechost = _pbs.ATTR_exechost
ATTR_execport = _pbs.ATTR_execport
ATTR_mtime = _pbs.ATTR_mtime
ATTR_qtime = _pbs.ATTR_qtime
ATTR_session = _pbs.ATTR_session
ATTR_euser = _pbs.ATTR_euser
ATTR_egroup = _pbs.ATTR_egroup
ATTR_hashname = _pbs.ATTR_hashname
ATTR_hopcount = _pbs.ATTR_hopcount
ATTR_security = _pbs.ATTR_security
ATTR_sched_hint = _pbs.ATTR_sched_hint
ATTR_substate = _pbs.ATTR_substate
ATTR_name = _pbs.ATTR_name
ATTR_owner = _pbs.ATTR_owner
ATTR_used = _pbs.ATTR_used
ATTR_state = _pbs.ATTR_state
ATTR_queue = _pbs.ATTR_queue
ATTR_server = _pbs.ATTR_server
ATTR_maxrun = _pbs.ATTR_maxrun
ATTR_maxreport = _pbs.ATTR_maxreport
ATTR_total = _pbs.ATTR_total
ATTR_comment = _pbs.ATTR_comment
ATTR_cookie = _pbs.ATTR_cookie
ATTR_qrank = _pbs.ATTR_qrank
ATTR_altid = _pbs.ATTR_altid
ATTR_etime = _pbs.ATTR_etime
ATTR_exitstat = _pbs.ATTR_exitstat
ATTR_forwardx11 = _pbs.ATTR_forwardx11
ATTR_submit_args = _pbs.ATTR_submit_args
ATTR_tokens = _pbs.ATTR_tokens
ATTR_netcounter = _pbs.ATTR_netcounter
ATTR_umask = _pbs.ATTR_umask
ATTR_start_time = _pbs.ATTR_start_time
ATTR_start_count = _pbs.ATTR_start_count
ATTR_checkpoint_dir = _pbs.ATTR_checkpoint_dir
ATTR_checkpoint_name = _pbs.ATTR_checkpoint_name
ATTR_checkpoint_time = _pbs.ATTR_checkpoint_time
ATTR_checkpoint_restart_status = _pbs.ATTR_checkpoint_restart_status
ATTR_restart_name = _pbs.ATTR_restart_name
ATTR_comp_time = _pbs.ATTR_comp_time
ATTR_reported = _pbs.ATTR_reported
ATTR_intcmd = _pbs.ATTR_intcmd
ATTR_job_radix = _pbs.ATTR_job_radix
ATTR_sister_list = _pbs.ATTR_sister_list
ATTR_total_runtime = _pbs.ATTR_total_runtime
ATTR_P = _pbs.ATTR_P
ATTR_node_exclusive = _pbs.ATTR_node_exclusive
ATTR_exec_gpus = _pbs.ATTR_exec_gpus
ATTR_exec_mics = _pbs.ATTR_exec_mics
ATTR_J = _pbs.ATTR_J
ATTR_pagg = _pbs.ATTR_pagg
ATTR_system_start_time = _pbs.ATTR_system_start_time
ATTR_gpu_flags = _pbs.ATTR_gpu_flags
ATTR_aclgren = _pbs.ATTR_aclgren
ATTR_aclgroup = _pbs.ATTR_aclgroup
ATTR_aclhten = _pbs.ATTR_aclhten
ATTR_aclhost = _pbs.ATTR_aclhost
ATTR_acluren = _pbs.ATTR_acluren
ATTR_acluser = _pbs.ATTR_acluser
ATTR_altrouter = _pbs.ATTR_altrouter
ATTR_checkpoint_min = _pbs.ATTR_checkpoint_min
ATTR_checkpoint_defaults = _pbs.ATTR_checkpoint_defaults
ATTR_enable = _pbs.ATTR_enable
ATTR_fromroute = _pbs.ATTR_fromroute
ATTR_hostlist = _pbs.ATTR_hostlist
ATTR_killdelay = _pbs.ATTR_killdelay
ATTR_maxgrprun = _pbs.ATTR_maxgrprun
ATTR_maxque = _pbs.ATTR_maxque
ATTR_maxuserque = _pbs.ATTR_maxuserque
ATTR_maxuserrun = _pbs.ATTR_maxuserrun
ATTR_qtype = _pbs.ATTR_qtype
ATTR_rescassn = _pbs.ATTR_rescassn
ATTR_rescdflt = _pbs.ATTR_rescdflt
ATTR_rescmax = _pbs.ATTR_rescmax
ATTR_rescmin = _pbs.ATTR_rescmin
ATTR_featreqd = _pbs.ATTR_featreqd
ATTR_req_login_property = _pbs.ATTR_req_login_property
ATTR_rerunnable = _pbs.ATTR_rerunnable
ATTR_rndzretry = _pbs.ATTR_rndzretry
ATTR_routedest = _pbs.ATTR_routedest
ATTR_routeheld = _pbs.ATTR_routeheld
ATTR_routewait = _pbs.ATTR_routewait
ATTR_routeretry = _pbs.ATTR_routeretry
ATTR_routelife = _pbs.ATTR_routelife
ATTR_rsvexpdt = _pbs.ATTR_rsvexpdt
ATTR_rsvsync = _pbs.ATTR_rsvsync
ATTR_start = _pbs.ATTR_start
ATTR_count = _pbs.ATTR_count
ATTR_number = _pbs.ATTR_number
ATTR_acllogic = _pbs.ATTR_acllogic
ATTR_aclgrpslpy = _pbs.ATTR_aclgrpslpy
ATTR_keepcompleted = _pbs.ATTR_keepcompleted
ATTR_disallowedtypes = _pbs.ATTR_disallowedtypes
ATTR_is_transit = _pbs.ATTR_is_transit
ATTR_aclroot = _pbs.ATTR_aclroot
ATTR_managers = _pbs.ATTR_managers
ATTR_dfltque = _pbs.ATTR_dfltque
ATTR_dispsvrsuffix = _pbs.ATTR_dispsvrsuffix
ATTR_jobsuffixalias = _pbs.ATTR_jobsuffixalias
ATTR_defnode = _pbs.ATTR_defnode
ATTR_locsvrs = _pbs.ATTR_locsvrs
ATTR_logevents = _pbs.ATTR_logevents
ATTR_logfile = _pbs.ATTR_logfile
ATTR_loglevel = _pbs.ATTR_loglevel
ATTR_mailfrom = _pbs.ATTR_mailfrom
ATTR_nodepack = _pbs.ATTR_nodepack
ATTR_nodesuffix = _pbs.ATTR_nodesuffix
ATTR_operators = _pbs.ATTR_operators
ATTR_queryother = _pbs.ATTR_queryother
ATTR_resccost = _pbs.ATTR_resccost
ATTR_rescavail = _pbs.ATTR_rescavail
ATTR_schedit = _pbs.ATTR_schedit
ATTR_scheduling = _pbs.ATTR_scheduling
ATTR_status = _pbs.ATTR_status
ATTR_syscost = _pbs.ATTR_syscost
ATTR_pingrate = _pbs.ATTR_pingrate
ATTR_ndchkrate = _pbs.ATTR_ndchkrate
ATTR_tcptimeout = _pbs.ATTR_tcptimeout
ATTR_jobstatrate = _pbs.ATTR_jobstatrate
ATTR_polljobs = _pbs.ATTR_polljobs
ATTR_downonerror = _pbs.ATTR_downonerror
ATTR_disableserveridcheck = _pbs.ATTR_disableserveridcheck
ATTR_jobnanny = _pbs.ATTR_jobnanny
ATTR_ownerpurge = _pbs.ATTR_ownerpurge
ATTR_qcqlimits = _pbs.ATTR_qcqlimits
ATTR_momjobsync = _pbs.ATTR_momjobsync
ATTR_maildomain = _pbs.ATTR_maildomain
ATTR_pbsversion = _pbs.ATTR_pbsversion
ATTR_submithosts = _pbs.ATTR_submithosts
ATTR_allownodesubmit = _pbs.ATTR_allownodesubmit
ATTR_allowproxyuser = _pbs.ATTR_allowproxyuser
ATTR_autonodenp = _pbs.ATTR_autonodenp
ATTR_servername = _pbs.ATTR_servername
ATTR_logfilemaxsize = _pbs.ATTR_logfilemaxsize
ATTR_logfilerolldepth = _pbs.ATTR_logfilerolldepth
ATTR_logkeepdays = _pbs.ATTR_logkeepdays
ATTR_nextjobnum = _pbs.ATTR_nextjobnum
ATTR_extraresc = _pbs.ATTR_extraresc
ATTR_schedversion = _pbs.ATTR_schedversion
ATTR_acctkeepdays = _pbs.ATTR_acctkeepdays
ATTR_lockfile = _pbs.ATTR_lockfile
ATTR_credentiallifetime = _pbs.ATTR_credentiallifetime
ATTR_jobmustreport = _pbs.ATTR_jobmustreport
ATTR_LockfileUpdateTime = _pbs.ATTR_LockfileUpdateTime
ATTR_LockfileCheckTime = _pbs.ATTR_LockfileCheckTime
ATTR_npdefault = _pbs.ATTR_npdefault
ATTR_clonebatchsize = _pbs.ATTR_clonebatchsize
ATTR_clonebatchdelay = _pbs.ATTR_clonebatchdelay
ATTR_jobstarttimeout = _pbs.ATTR_jobstarttimeout
ATTR_jobforcecanceltime = _pbs.ATTR_jobforcecanceltime
ATTR_maxarraysize = _pbs.ATTR_maxarraysize
ATTR_maxslotlimit = _pbs.ATTR_maxslotlimit
ATTR_recordjobinfo = _pbs.ATTR_recordjobinfo
ATTR_recordjobscript = _pbs.ATTR_recordjobscript
ATTR_joblogfilemaxsize = _pbs.ATTR_joblogfilemaxsize
ATTR_joblogfilerolldepth = _pbs.ATTR_joblogfilerolldepth
ATTR_joblogkeepdays = _pbs.ATTR_joblogkeepdays
ATTR_minthreads = _pbs.ATTR_minthreads
ATTR_maxthreads = _pbs.ATTR_maxthreads
ATTR_threadidleseconds = _pbs.ATTR_threadidleseconds
ATTR_moabarraycompatible = _pbs.ATTR_moabarraycompatible
ATTR_nomailforce = _pbs.ATTR_nomailforce
ATTR_interactivejobscanroam = _pbs.ATTR_interactivejobscanroam
ATTR_crayenabled = _pbs.ATTR_crayenabled
ATTR_nppcu = _pbs.ATTR_nppcu
ATTR_login_node_key = _pbs.ATTR_login_node_key
ATTR_maxuserqueuable = _pbs.ATTR_maxuserqueuable
ATTR_automaticrequeueexitcode = _pbs.ATTR_automaticrequeueexitcode
ATTR_jobsynctimeout = _pbs.ATTR_jobsynctimeout
ATTR_pass_cpu_clock = _pbs.ATTR_pass_cpu_clock
ATTR_NODE_state = _pbs.ATTR_NODE_state
ATTR_NODE_power_state = _pbs.ATTR_NODE_power_state
ATTR_NODE_np = _pbs.ATTR_NODE_np
ATTR_NODE_properties = _pbs.ATTR_NODE_properties
ATTR_NODE_ntype = _pbs.ATTR_NODE_ntype
ATTR_NODE_jobs = _pbs.ATTR_NODE_jobs
ATTR_NODE_status = _pbs.ATTR_NODE_status
ATTR_NODE_note = _pbs.ATTR_NODE_note
ATTR_NODE_mom_port = _pbs.ATTR_NODE_mom_port
ATTR_NODE_mom_rm_port = _pbs.ATTR_NODE_mom_rm_port
ATTR_NODE_num_node_boards = _pbs.ATTR_NODE_num_node_boards
ATTR_NODE_numa_str = _pbs.ATTR_NODE_numa_str
ATTR_NODE_gpus = _pbs.ATTR_NODE_gpus
ATTR_NODE_gpustatus = _pbs.ATTR_NODE_gpustatus
ATTR_NODE_gpus_str = _pbs.ATTR_NODE_gpus_str
ATTR_NODE_mics = _pbs.ATTR_NODE_mics
ATTR_NODE_micstatus = _pbs.ATTR_NODE_micstatus
ATTR_copy_on_rerun = _pbs.ATTR_copy_on_rerun
ATTR_job_exclusive_on_use = _pbs.ATTR_job_exclusive_on_use
ATTR_mailsubjectfmt = _pbs.ATTR_mailsubjectfmt
ATTR_mailbodyfmt = _pbs.ATTR_mailbodyfmt
CHECKPOINT_UNSPECIFIED = _pbs.CHECKPOINT_UNSPECIFIED
NO_HOLD = _pbs.NO_HOLD
NO_JOIN = _pbs.NO_JOIN
NO_KEEP = _pbs.NO_KEEP
MAIL_AT_ABORT = _pbs.MAIL_AT_ABORT
DEFAULT_PRIORITY = _pbs.DEFAULT_PRIORITY
ARRAY_RANGE = _pbs.ARRAY_RANGE
DELDELAY = _pbs.DELDELAY
DELPURGE = _pbs.DELPURGE
DELASYNC = _pbs.DELASYNC
PURGECOMP = _pbs.PURGECOMP
EXECQUEONLY = _pbs.EXECQUEONLY
RERUNFORCE = _pbs.RERUNFORCE
USER_HOLD = _pbs.USER_HOLD
OTHER_HOLD = _pbs.OTHER_HOLD
SYSTEM_HOLD = _pbs.SYSTEM_HOLD
ND_free = _pbs.ND_free
ND_offline = _pbs.ND_offline
ND_down = _pbs.ND_down
ND_reserve = _pbs.ND_reserve
ND_job_exclusive = _pbs.ND_job_exclusive
ND_job_sharing = _pbs.ND_job_sharing
ND_busy = _pbs.ND_busy
ND_state_unknown = _pbs.ND_state_unknown
ND_running = _pbs.ND_running
ND_standby = _pbs.ND_standby
ND_suspend = _pbs.ND_suspend
ND_sleep = _pbs.ND_sleep
ND_hibernate = _pbs.ND_hibernate
ND_shutdown = _pbs.ND_shutdown
ND_active = _pbs.ND_active
ND_all = _pbs.ND_all
ND_up = _pbs.ND_up
ND_timeshared = _pbs.ND_timeshared
ND_cluster = _pbs.ND_cluster
Q_DT_batch = _pbs.Q_DT_batch
Q_DT_interactive = _pbs.Q_DT_interactive
Q_DT_rerunable = _pbs.Q_DT_rerunable
Q_DT_nonrerunable = _pbs.Q_DT_nonrerunable
Q_DT_fault_tolerant = _pbs.Q_DT_fault_tolerant
Q_DT_fault_intolerant = _pbs.Q_DT_fault_intolerant
Q_DT_job_array = _pbs.Q_DT_job_array
MAX_ENCODE_BFR = _pbs.MAX_ENCODE_BFR
MGR_CMD_CREATE = _pbs.MGR_CMD_CREATE
MGR_CMD_DELETE = _pbs.MGR_CMD_DELETE
MGR_CMD_SET = _pbs.MGR_CMD_SET
MGR_CMD_UNSET = _pbs.MGR_CMD_UNSET
MGR_CMD_LIST = _pbs.MGR_CMD_LIST
MGR_CMD_PRINT = _pbs.MGR_CMD_PRINT
MGR_CMD_ACTIVE = _pbs.MGR_CMD_ACTIVE
MGR_OBJ_NONE = _pbs.MGR_OBJ_NONE
MGR_OBJ_SERVER = _pbs.MGR_OBJ_SERVER
MGR_OBJ_QUEUE = _pbs.MGR_OBJ_QUEUE
MGR_OBJ_JOB = _pbs.MGR_OBJ_JOB
MGR_OBJ_NODE = _pbs.MGR_OBJ_NODE
MSG_OUT = _pbs.MSG_OUT
MSG_ERR = _pbs.MSG_ERR
SHUT_SIG = _pbs.SHUT_SIG
SHUT_IMMEDIATE = _pbs.SHUT_IMMEDIATE
SHUT_DELAY = _pbs.SHUT_DELAY
SHUT_QUICK = _pbs.SHUT_QUICK
SIG_RESUME = _pbs.SIG_RESUME
SIG_SUSPEND = _pbs.SIG_SUSPEND
PBS_MAXHOSTNAME = _pbs.PBS_MAXHOSTNAME
MAXPATHLEN = _pbs.MAXPATHLEN
MAXPORTLEN = _pbs.MAXPORTLEN
MAXNAMLEN = _pbs.MAXNAMLEN
MAX_NOTE = _pbs.MAX_NOTE
MAX_NOTE_STR = _pbs.MAX_NOTE_STR
PBS_MAXUSER = _pbs.PBS_MAXUSER
PBS_MAXGRPN = _pbs.PBS_MAXGRPN
PBS_MAXGPUID = _pbs.PBS_MAXGPUID
PBS_MAXQUEUENAME = _pbs.PBS_MAXQUEUENAME
PBS_MAXSERVERNAME = _pbs.PBS_MAXSERVERNAME
PBS_MAXJOBARRAYLEN = _pbs.PBS_MAXJOBARRAYLEN
PBS_MAXSEQNUM = _pbs.PBS_MAXSEQNUM
PBS_MAXPORTNUM = _pbs.PBS_MAXPORTNUM
PBS_MAXJOBARRAY = _pbs.PBS_MAXJOBARRAY
PBS_MAXSVRJOBID = _pbs.PBS_MAXSVRJOBID
PBS_MAXCLTJOBID = _pbs.PBS_MAXCLTJOBID
PBS_MAXDEST = _pbs.PBS_MAXDEST
PBS_MAXROUTEDEST = _pbs.PBS_MAXROUTEDEST
PBS_USE_IFF = _pbs.PBS_USE_IFF
PBS_INTERACTIVE = _pbs.PBS_INTERACTIVE
PBS_TERM_BUF_SZ = _pbs.PBS_TERM_BUF_SZ
PBS_TERM_CCA = _pbs.PBS_TERM_CCA
PBS_MAXCREDENTIAL_LEN = _pbs.PBS_MAXCREDENTIAL_LEN
PBS_QS_VERSION_BASE = _pbs.PBS_QS_VERSION_BASE
PBS_QS_VERSION_INT = _pbs.PBS_QS_VERSION_INT
PBS_QS_VERSION = _pbs.PBS_QS_VERSION
PBS_BATCH_SERVICE_NAME = _pbs.PBS_BATCH_SERVICE_NAME
PBS_BATCH_SERVICE_PORT = _pbs.PBS_BATCH_SERVICE_PORT
PBS_BATCH_SERVICE_NAME_DIS = _pbs.PBS_BATCH_SERVICE_NAME_DIS
PBS_MOM_SERVICE_NAME = _pbs.PBS_MOM_SERVICE_NAME
PBS_MOM_SERVICE_PORT = _pbs.PBS_MOM_SERVICE_PORT
PBS_MANAGER_SERVICE_NAME = _pbs.PBS_MANAGER_SERVICE_NAME
PBS_MANAGER_SERVICE_PORT = _pbs.PBS_MANAGER_SERVICE_PORT
PBS_SCHEDULER_SERVICE_NAME = _pbs.PBS_SCHEDULER_SERVICE_NAME
PBS_SCHEDULER_SERVICE_PORT = _pbs.PBS_SCHEDULER_SERVICE_PORT
TRQ_AUTHD_SERVICE_PORT = _pbs.TRQ_AUTHD_SERVICE_PORT
CHECKPOINTHOLD = _pbs.CHECKPOINTHOLD
CHECKPOINTCONT = _pbs.CHECKPOINTCONT
MOM_DEFAULT_CHECKPOINT_DIR = _pbs.MOM_DEFAULT_CHECKPOINT_DIR
NO_MOM_RELAY = _pbs.NO_MOM_RELAY
SET = _pbs.SET
UNSET = _pbs.UNSET
INCR = _pbs.INCR
DECR = _pbs.DECR
EQ = _pbs.EQ
NE = _pbs.NE
GE = _pbs.GE
GT = _pbs.GT
LE = _pbs.LE
LT = _pbs.LT
DFLT = _pbs.DFLT
MERGE = _pbs.MERGE
INCR_OLD = _pbs.INCR_OLD
NPPCU_ALPS_CHOOSES = _pbs.NPPCU_ALPS_CHOOSES
NPPCU_NO_USE_HT = _pbs.NPPCU_NO_USE_HT
NPPCU_USE_HT = _pbs.NPPCU_USE_HT
class attrl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, attrl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, attrl, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_setmethods__["next"] = _pbs.attrl_next_set
    __swig_getmethods__["next"] = _pbs.attrl_next_get
    if _newclass:next = _swig_property(_pbs.attrl_next_get, _pbs.attrl_next_set)
    __swig_setmethods__["name"] = _pbs.attrl_name_set
    __swig_getmethods__["name"] = _pbs.attrl_name_get
    if _newclass:name = _swig_property(_pbs.attrl_name_get, _pbs.attrl_name_set)
    __swig_setmethods__["resource"] = _pbs.attrl_resource_set
    __swig_getmethods__["resource"] = _pbs.attrl_resource_get
    if _newclass:resource = _swig_property(_pbs.attrl_resource_get, _pbs.attrl_resource_set)
    __swig_setmethods__["value"] = _pbs.attrl_value_set
    __swig_getmethods__["value"] = _pbs.attrl_value_get
    if _newclass:value = _swig_property(_pbs.attrl_value_get, _pbs.attrl_value_set)
    __swig_setmethods__["op"] = _pbs.attrl_op_set
    __swig_getmethods__["op"] = _pbs.attrl_op_get
    if _newclass:op = _swig_property(_pbs.attrl_op_get, _pbs.attrl_op_set)
    def __str__(self): return _pbs.attrl___str__(self)
    __swig_destroy__ = _pbs.delete_attrl
    __del__ = lambda self : None;
attrl_swigregister = _pbs.attrl_swigregister
attrl_swigregister(attrl)

class attropl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, attropl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, attropl, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_setmethods__["next"] = _pbs.attropl_next_set
    __swig_getmethods__["next"] = _pbs.attropl_next_get
    if _newclass:next = _swig_property(_pbs.attropl_next_get, _pbs.attropl_next_set)
    __swig_setmethods__["name"] = _pbs.attropl_name_set
    __swig_getmethods__["name"] = _pbs.attropl_name_get
    if _newclass:name = _swig_property(_pbs.attropl_name_get, _pbs.attropl_name_set)
    __swig_setmethods__["resource"] = _pbs.attropl_resource_set
    __swig_getmethods__["resource"] = _pbs.attropl_resource_get
    if _newclass:resource = _swig_property(_pbs.attropl_resource_get, _pbs.attropl_resource_set)
    __swig_setmethods__["value"] = _pbs.attropl_value_set
    __swig_getmethods__["value"] = _pbs.attropl_value_get
    if _newclass:value = _swig_property(_pbs.attropl_value_get, _pbs.attropl_value_set)
    __swig_setmethods__["op"] = _pbs.attropl_op_set
    __swig_getmethods__["op"] = _pbs.attropl_op_get
    if _newclass:op = _swig_property(_pbs.attropl_op_get, _pbs.attropl_op_set)
    def __str__(self): return _pbs.attropl___str__(self)
    __swig_destroy__ = _pbs.delete_attropl
    __del__ = lambda self : None;
attropl_swigregister = _pbs.attropl_swigregister
attropl_swigregister(attropl)

class batch_status(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, batch_status, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, batch_status, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_setmethods__["next"] = _pbs.batch_status_next_set
    __swig_getmethods__["next"] = _pbs.batch_status_next_get
    if _newclass:next = _swig_property(_pbs.batch_status_next_get, _pbs.batch_status_next_set)
    __swig_setmethods__["name"] = _pbs.batch_status_name_set
    __swig_getmethods__["name"] = _pbs.batch_status_name_get
    if _newclass:name = _swig_property(_pbs.batch_status_name_get, _pbs.batch_status_name_set)
    __swig_setmethods__["attribs"] = _pbs.batch_status_attribs_set
    __swig_getmethods__["attribs"] = _pbs.batch_status_attribs_get
    if _newclass:attribs = _swig_property(_pbs.batch_status_attribs_get, _pbs.batch_status_attribs_set)
    __swig_setmethods__["text"] = _pbs.batch_status_text_set
    __swig_getmethods__["text"] = _pbs.batch_status_text_get
    if _newclass:text = _swig_property(_pbs.batch_status_text_get, _pbs.batch_status_text_set)
batch_status_swigregister = _pbs.batch_status_swigregister
batch_status_swigregister(batch_status)


def avail(*args):
  return _pbs.avail(*args)
avail = _pbs.avail

def pbs_asyrunjob(*args):
  return _pbs.pbs_asyrunjob(*args)
pbs_asyrunjob = _pbs.pbs_asyrunjob

def pbs_alterjob_async(*args):
  return _pbs.pbs_alterjob_async(*args)
pbs_alterjob_async = _pbs.pbs_alterjob_async

def pbs_alterjob(*args):
  return _pbs.pbs_alterjob(*args)
pbs_alterjob = _pbs.pbs_alterjob

def pbs_connect(*args):
  return _pbs.pbs_connect(*args)
pbs_connect = _pbs.pbs_connect

def pbs_query_max_connections():
  return _pbs.pbs_query_max_connections()
pbs_query_max_connections = _pbs.pbs_query_max_connections

def pbs_default():
  return _pbs.pbs_default()
pbs_default = _pbs.pbs_default

def pbs_fbserver():
  return _pbs.pbs_fbserver()
pbs_fbserver = _pbs.pbs_fbserver

def pbs_get_server_list():
  return _pbs.pbs_get_server_list()
pbs_get_server_list = _pbs.pbs_get_server_list

def pbs_deljob(*args):
  return _pbs.pbs_deljob(*args)
pbs_deljob = _pbs.pbs_deljob

def pbs_disconnect(*args):
  return _pbs.pbs_disconnect(*args)
pbs_disconnect = _pbs.pbs_disconnect

def pbs_geterrmsg(*args):
  return _pbs.pbs_geterrmsg(*args)
pbs_geterrmsg = _pbs.pbs_geterrmsg

def pbs_holdjob(*args):
  return _pbs.pbs_holdjob(*args)
pbs_holdjob = _pbs.pbs_holdjob

def pbs_checkpointjob(*args):
  return _pbs.pbs_checkpointjob(*args)
pbs_checkpointjob = _pbs.pbs_checkpointjob

def pbs_locjob(*args):
  return _pbs.pbs_locjob(*args)
pbs_locjob = _pbs.pbs_locjob

def pbs_manager(*args):
  return _pbs.pbs_manager(*args)
pbs_manager = _pbs.pbs_manager

def pbs_movejob(*args):
  return _pbs.pbs_movejob(*args)
pbs_movejob = _pbs.pbs_movejob

def pbs_msgjob(*args):
  return _pbs.pbs_msgjob(*args)
pbs_msgjob = _pbs.pbs_msgjob

def pbs_orderjob(*args):
  return _pbs.pbs_orderjob(*args)
pbs_orderjob = _pbs.pbs_orderjob

def pbs_rescquery(*args):
  return _pbs.pbs_rescquery(*args)
pbs_rescquery = _pbs.pbs_rescquery

def pbs_rescreserve(*args):
  return _pbs.pbs_rescreserve(*args)
pbs_rescreserve = _pbs.pbs_rescreserve

def pbs_rescrelease(*args):
  return _pbs.pbs_rescrelease(*args)
pbs_rescrelease = _pbs.pbs_rescrelease

def pbs_rerunjob(*args):
  return _pbs.pbs_rerunjob(*args)
pbs_rerunjob = _pbs.pbs_rerunjob

def pbs_rlsjob(*args):
  return _pbs.pbs_rlsjob(*args)
pbs_rlsjob = _pbs.pbs_rlsjob

def pbs_runjob(*args):
  return _pbs.pbs_runjob(*args)
pbs_runjob = _pbs.pbs_runjob

def pbs_selectjob(*args):
  return _pbs.pbs_selectjob(*args)
pbs_selectjob = _pbs.pbs_selectjob

def pbs_sigjob(*args):
  return _pbs.pbs_sigjob(*args)
pbs_sigjob = _pbs.pbs_sigjob

def pbs_sigjobasync(*args):
  return _pbs.pbs_sigjobasync(*args)
pbs_sigjobasync = _pbs.pbs_sigjobasync

def pbs_statfree(*args):
  return _pbs.pbs_statfree(*args)
pbs_statfree = _pbs.pbs_statfree

def pbs_statjob(*args):
  return _pbs.pbs_statjob(*args)
pbs_statjob = _pbs.pbs_statjob

def pbs_selstat(*args):
  return _pbs.pbs_selstat(*args)
pbs_selstat = _pbs.pbs_selstat

def pbs_statque(*args):
  return _pbs.pbs_statque(*args)
pbs_statque = _pbs.pbs_statque

def pbs_statserver(*args):
  return _pbs.pbs_statserver(*args)
pbs_statserver = _pbs.pbs_statserver

def pbs_statnode(*args):
  return _pbs.pbs_statnode(*args)
pbs_statnode = _pbs.pbs_statnode

def pbs_submit(*args):
  return _pbs.pbs_submit(*args)
pbs_submit = _pbs.pbs_submit

def pbs_submit_hash_ext(*args):
  return _pbs.pbs_submit_hash_ext(*args)
pbs_submit_hash_ext = _pbs.pbs_submit_hash_ext

def pbs_terminate(*args):
  return _pbs.pbs_terminate(*args)
pbs_terminate = _pbs.pbs_terminate

def totpool(*args):
  return _pbs.totpool(*args)
totpool = _pbs.totpool

def usepool(*args):
  return _pbs.usepool(*args)
usepool = _pbs.usepool

def pbs_gpumode(*args):
  return _pbs.pbs_gpumode(*args)
pbs_gpumode = _pbs.pbs_gpumode

def trq_set_preferred_network_interface(*args):
  return _pbs.trq_set_preferred_network_interface(*args)
trq_set_preferred_network_interface = _pbs.trq_set_preferred_network_interface

def trq_get_if_name():
  return _pbs.trq_get_if_name()
trq_get_if_name = _pbs.trq_get_if_name

def pbs_stagein(*args):
  return _pbs.pbs_stagein(*args)
pbs_stagein = _pbs.pbs_stagein

def openrm(*args):
  return _pbs.openrm(*args)
openrm = _pbs.openrm

def closerm_err(*args):
  return _pbs.closerm_err(*args)
closerm_err = _pbs.closerm_err

def closerm(*args):
  return _pbs.closerm(*args)
closerm = _pbs.closerm

def downrm(*args):
  return _pbs.downrm(*args)
downrm = _pbs.downrm

def configrm(*args):
  return _pbs.configrm(*args)
configrm = _pbs.configrm

def addreq_err(*args):
  return _pbs.addreq_err(*args)
addreq_err = _pbs.addreq_err

def begin_rm_req(*args):
  return _pbs.begin_rm_req(*args)
begin_rm_req = _pbs.begin_rm_req

def addreq(*args):
  return _pbs.addreq(*args)
addreq = _pbs.addreq

def allreq(*args):
  return _pbs.allreq(*args)
allreq = _pbs.allreq

def getreq_err(*args):
  return _pbs.getreq_err(*args)
getreq_err = _pbs.getreq_err

def getreq(*args):
  return _pbs.getreq(*args)
getreq = _pbs.getreq

def flushreq():
  return _pbs.flushreq()
flushreq = _pbs.flushreq

def activereq():
  return _pbs.activereq()
activereq = _pbs.activereq

def fullresp(*args):
  return _pbs.fullresp(*args)
fullresp = _pbs.fullresp
LOG_BUF_SIZE = _pbs.LOG_BUF_SIZE
LOCAL_LOG_BUF_SIZE = _pbs.LOCAL_LOG_BUF_SIZE
LOG_EMERG = _pbs.LOG_EMERG
LOG_ALERT = _pbs.LOG_ALERT
LOG_CRIT = _pbs.LOG_CRIT
LOG_ERR = _pbs.LOG_ERR
LOG_WARNING = _pbs.LOG_WARNING
LOG_NOTICE = _pbs.LOG_NOTICE
LOG_INFO = _pbs.LOG_INFO
LOG_DEBUG = _pbs.LOG_DEBUG
MAXLINE = _pbs.MAXLINE
GETV = _pbs.GETV
SETV = _pbs.SETV

def log_err(*args):
  return _pbs.log_err(*args)
log_err = _pbs.log_err

def log_ext(*args):
  return _pbs.log_ext(*args)
log_ext = _pbs.log_ext

def log_event(*args):
  return _pbs.log_event(*args)
log_event = _pbs.log_event

def log_record(*args):
  return _pbs.log_record(*args)
log_record = _pbs.log_record

def log_available(*args):
  return _pbs.log_available(*args)
log_available = _pbs.log_available

def log_init(*args):
  return _pbs.log_init(*args)
log_init = _pbs.log_init

def chk_file_sec(*args):
  return _pbs.chk_file_sec(*args)
chk_file_sec = _pbs.chk_file_sec
PBSEVENT_ERROR = _pbs.PBSEVENT_ERROR
PBSEVENT_SYSTEM = _pbs.PBSEVENT_SYSTEM
PBSEVENT_ADMIN = _pbs.PBSEVENT_ADMIN
PBSEVENT_JOB = _pbs.PBSEVENT_JOB
PBSEVENT_JOB_USAGE = _pbs.PBSEVENT_JOB_USAGE
PBSEVENT_SECURITY = _pbs.PBSEVENT_SECURITY
PBSEVENT_SCHED = _pbs.PBSEVENT_SCHED
PBSEVENT_DEBUG = _pbs.PBSEVENT_DEBUG
PBSEVENT_DEBUG2 = _pbs.PBSEVENT_DEBUG2
PBSEVENT_CLIENTAUTH = _pbs.PBSEVENT_CLIENTAUTH
PBSEVENT_SYSLOG = _pbs.PBSEVENT_SYSLOG
PBSEVENT_FORCE = _pbs.PBSEVENT_FORCE
PBS_EVENTCLASS_SERVER = _pbs.PBS_EVENTCLASS_SERVER
PBS_EVENTCLASS_QUEUE = _pbs.PBS_EVENTCLASS_QUEUE
PBS_EVENTCLASS_JOB = _pbs.PBS_EVENTCLASS_JOB
PBS_EVENTCLASS_REQUEST = _pbs.PBS_EVENTCLASS_REQUEST
PBS_EVENTCLASS_FILE = _pbs.PBS_EVENTCLASS_FILE
PBS_EVENTCLASS_ACCT = _pbs.PBS_EVENTCLASS_ACCT
PBS_EVENTCLASS_NODE = _pbs.PBS_EVENTCLASS_NODE
PBS_EVENTCLASS_TRQAUTHD = _pbs.PBS_EVENTCLASS_TRQAUTHD
PBSEVENT_MASK = _pbs.PBSEVENT_MASK
MAX_PATH_LEN = _pbs.MAX_PATH_LEN
SECS_PER_DAY = _pbs.SECS_PER_DAY
TRUE = _pbs.TRUE
FALSE = _pbs.FALSE
PBSE_TOTAL_CEILING = _pbs.PBSE_TOTAL_CEILING
PBSE_ = _pbs.PBSE_
PBSE_NONE = _pbs.PBSE_NONE

def pbse_to_txt(*args):
  return _pbs.pbse_to_txt(*args)
pbse_to_txt = _pbs.pbse_to_txt

def pbs_strerror(*args):
  return _pbs.pbs_strerror(*args)
pbs_strerror = _pbs.pbs_strerror
#  PBS python interface
#  Author: Bas van der Vlies <bas.vandervlies@surfsara.nl>
#  Date  : 27 Feb 2002
#  Desc. : This is python wrapper class for getting the resource
#          mom values.
#
# CVS info
# $Id: resmom.py,v 1.6 2002/10/21 14:14:47 sscpbas Exp $
# $Date: 2002/10/21 14:14:47 $
# $Revision: 1.6 $
#
import string
import types

# Default linux resources to get from the mom
#
default_linux_res = [   
    "availmem",	    # available memory size in KB
    "ideal_load",	# static ideal_load value
    "loadave",      # the current load average
    "max_load",	    # static max_load value
    "ncpus",        # number of cpus 
    "physmem",      # physical memory size in KB
    "resi",		    # resident memory size for a pid or session in KB
    "totmem",	    # total memory size in KB
    "walltime",	    # wall clock time for a pid
]

# Default irix6 resources to get from the mom
#
default_irix6_res = [   
    "availmem",	# available memory size in KB
    "loadave",      # the current load average
    "ncpus",        # number of cpus
    "physmem",      # physical memory size in KB
    "resi",		# resident memory size for a pid or session in KB
    "walltime",	# wall clock time for a pid
    "quota",	# quota information (sizes in KB)
]

default_mom_res = [   
    "arch",		# the architecture of the machine
    "uname",	# the architecture of the machine
    "cput",		# cpu time for a pid or session
    "idletime",	# seconds of idle time
    "mem",		# memory size for a pid or session in KB
    "sessions",	# list of sessions in the system
    "pids",         # list of pids in a session
    "nsessions",	# number of sessions in the system
    "nusers",	# number of users in the system
    "size",		# size of a file or filesystem
    "host",		# Name  of host on which job should be run 
    "nodes",	# Number and/or type of nodes to be reserved for exclusive use by the job
    "other",	# Allows a  user  to  specify  site  specific  information
    "software",	# Allows a user to specify software required by the job
]

def check_resp(dict, str):
  """
  Check the daemon response. If we have no permission to
  query the values then we got a 'None' response. Else
  if we supplied a keyword that does not exits we get a
  '?' response
  """
  if not str:
    return
  
  ## Value can contain the '=' char :-(
  #  
  l =  string.split(str, '=')
  key = string.strip(l[0])
  if len(l) > 2:
    val = string.strip( '='.join(l[1:]) )
  else:
    val = string.strip(l[1])

  key = string.strip(key)
  val = string.strip(val)

  # Did we got a valid response
  #
  if not val[0] == '?':
    dict[key] = val

def use_default_keywords(id, d):
  """
  Get the default values from the mom daemon
  """
  err = 0
  print default_mom_res
  for res in default_mom_res:
    print res
    #addreq(id, res)
    addreq_err(id, err, res) 
    print err
    #resp = getreq(id)
    resp = getreq_err(err, id)
    print "error: ", err

    print resp,id
    check_resp(d, resp)

  # Do not proceed if we have an empty dictionary
  #
  if not d:
    return

  if d['arch' ] == 'linux':
    for res in default_linux_res:
      addreq(id, res)
      resp = getreq(id)
      check_resp(d, resp)

def use_user_keywords(id, d, l):
  for res in l:
    if type(res) is types.StringType:
      addreq(id, res)
      resp = getreq(id)
      check_resp(d, resp)
    else:
      raise TypeError, 'Expected a string got %s :%s' %(type(res), res) 

def get_mom_values(id, list = None):
  """
  This function will query the mom with a default resmon keywords
  and 'arch' depended keywords. Supported archs are:
    linux
    irix6
  User can also supply their own list of keywords as second parameter.
  arguments:
    id   : connection number with mom daemon on a node
    list : optional parameter. If supplied then use this. A list
           of mom keywords.
  """

  d = {}
  if not list:
    use_default_keywords(id, d)
  else:
    use_user_keywords(id, d , list)
     
  return d

version_info = ( 4, 4, 0 )
version = 'SARA pbs_python version 4.4.0'

## A useful dict with error codes to text
#
# Author: Bas van der Vlies <bas.vandervlies@surfsara.nl>
#
# SVN Info:
#	$Id: errors.py 429 2005-11-04 13:59:06Z bas $
#

def error():
  """
  Check if there is an error, if so fetch the error message string. 
  It says more then a number!
  """
  e = get_error()
  return (e, pbs_strerror(e))
#     return (e, errors_txt[e])
#  else:
#     return (e, "Could not find a text for this error, uhhh")

# This file is compatible with both classic and new-style classes.

cvar = _pbs.cvar

