# pip install prettytable

from prettytable import PrettyTable
mytable = PrettyTable(["Student Name","Class","Section","Percentage"])

mytable.add_row(["Appu","x","B","91.2%"])
mytable.add_row(["Pappu","X","C","63.5%"])
mytable.add_row(["Jhappu","X","A","98.32%"])
mytable.add_row(["Popaat","X","D","2.7%"])
mytable.add_row(["Pupu","X","A","98.2%"])
mytable.add_row(["Rajniganda","X","B","88.1%"])
mytable.add_row(["Amy","X","B","95.8%"])

print(mytable)
