from django.shortcuts import render
from .Container import random_IP, check_ip, df_good_valid_ip
import ipaddress
import pandas as pd

def index(request):
      good_ip = {ipaddress.ip_address(i) for i in df_good_valid_ip['IP'].values}

      ip_list, Permission, Reason, type_lst = [], [], [], []

      for _ in range(10):
          row = random_IP()
          row_ip = row[0]
          type_IP = row[1]

          result, flag = check_ip(row_ip, good_ip)

          ip_list.append(row_ip)
          Permission.append(flag)
          Reason.append(result)
          type_lst.append(type_IP)

      df = pd.DataFrame({
          'IP': ip_list,
          'Permission': Permission,
          'type': type_lst,
          'Reason': Reason
      })

      table_data = df.to_dict(orient='records')

      allowed = len(df[df['Permission'] == True])
      denied = len(df[df['Permission'] == False])

      # для круговой диаграммы
      type_counts = df['type'].value_counts().to_dict()

      return render(request, 'container.html', {
          'table': table_data,
          'allowed': allowed,
          'denied': denied,
          'type_counts': type_counts
      })