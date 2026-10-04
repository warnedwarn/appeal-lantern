from pathlib import Path
import json,re,subprocess,time
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions

R=Path(__file__).parents[1];ROOT=R.parents[3]
def env(name):
 text=(ROOT/'accounts.env').read_text();m=re.search(r'^'+re.escape(name)+r'\s*=\s*"?([^"\r\n]+)',text,re.M);return m.group(1).strip()
def calldata(method=None,args=None,kwargs=None):
 out={}
 if method is not None:out['method']=method
 if args:out['args']=args
 if kwargs:out['kwargs']=kwargs
 return out
contract_actions.make_calldata_object=calldata
accounts=[create_account(account_private_key=env('ACCOUNT_'+str(i)+'_GENLAYER_PRIVATE_KEY')) for i in (1,2,3)];clients=[create_client(chain=studionet,account=a) for a in accounts];address=json.loads((R/'deployment.json').read_text())['contractAddress'];sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();stamp=str(int(time.time()));case='APPEAL-'+stamp
raw='https://raw.githubusercontent.com/warnedwarn/appeal-lantern/'+sha+'/evidence/';cdn='https://cdn.jsdelivr.net/gh/warnedwarn/appeal-lantern@'+sha+'/evidence/'
def send(client,method,args):
 tx=client.write_contract(address=address,function_name=method,args=args);client.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000);full=client.get_transaction(transaction_hash=tx);leader=(full.get('consensus_data',{}).get('leader_receipt')or[{}])[0];assert full.get('result_name')=='MAJORITY_AGREE' and leader.get('execution_result')=='SUCCESS',full;return str(tx)
txs={};txs['open']=send(clients[1],'open_audit',[case,accounts[0].address,accounts[2].address,'Permit 17 suspension',raw+'rulebook.md',cdn+'decision.md',['FORUM','DEADLINE','METHOD','FORM','FEE','CONTACT'],900]);txs['inspect']=send(clients[2],'inspect_notice',[case]);mid=clients[1].read_contract(address=address,function_name='get_audit',args=[case]);assert mid['state']=='DEFECTIVE',mid;txs['cure']=send(clients[0],'cure_notice',[case,cdn+'decision-corrected.md']);state=clients[1].read_contract(address=address,function_name='get_audit',args=[case]);assert state['state']=='CURED',state;out={'caseId':case,'transactions':txs,'state':state,'walletDisclosure':'All three demo wallets and fixture files are operator-controlled.'};(R/'network-run.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
