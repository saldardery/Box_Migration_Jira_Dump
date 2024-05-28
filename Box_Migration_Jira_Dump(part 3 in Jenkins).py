import pandas as pd
Migration_Targets = 'C:\\Users\\powerbi\\Box\\Incorta Backend\\Migration Targets Incorta.csv'
Migration_Jira_Dump = 'C:\\Users\\powerbi\\Box\\Incorta Backend\\Migration Jira Dump.csv'

Migration_Targets = pd.read_csv(Migration_Targets)
Migration_Jira_Dump=pd.read_csv(Migration_Jira_Dump)

i=0
for itterate in Migration_Targets.iterrows():
  z=0
  Sum_of_Hosts=0
  for itterate_dump in Migration_Jira_Dump.iterrows():
    Jira_Column = Migration_Targets.loc[i, 'Jira Column']
    if((str(Migration_Targets.loc[i,'Product']).lower()==str(Migration_Jira_Dump.loc[z,'Custom field (Product)']).lower()) and (Migration_Jira_Dump.loc[z,Jira_Column] >0)):

         Sum_of_Hosts=Sum_of_Hosts+Migration_Jira_Dump.loc[z,Jira_Column]

    z = z + 1
  Migration_Targets.loc[i,'Host Count']=Sum_of_Hosts

  i=i+1

Migration_Targets.to_csv('C:\\Users\\powerbi\\Box\\Incorta Backend\\Migration Targets Incorta.csv',index=False)
Migration_Targets.to_csv('C:\\Users\\powerbi\\Box\\SW Migrations\\Migration Targets Incorta.csv',index=False)
