import cx_Oracle

#################################################################################
### ORACLE 12C CONNECTION
# dsn_tns = cx_Oracle.makedsn('10.11.201.55', '1525', service_name='testpdb')
# con = cx_Oracle.connect(user=r'shifullah', password='shifullah', dsn=dsn_tns)
#################################################################################

###############################################################################
### ORACLE 11G CONNECTION
con = cx_Oracle.connect('shifullah/shifullah@10.11.201.251:1521/stlbas')
###############################################################################
cur = con.cursor()

a = 40
b = 10
c = cur.var(cx_Oracle.NUMBER)
cur.callproc('test_addition', [a, b, c])
print ("Total summation is: ", c.getvalue())

cur.close()
con.close()