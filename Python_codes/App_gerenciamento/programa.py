from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()
db = sqlite3.connect('adm.db')
cursor_db = db.cursor()
cursor_db.close()
db.commit()
db.close()


class Funcs():
    def __init__(self):
        self.lista_vendas = root.Listbox(self)
        self.lista_vendas.pac                      
        self.lista_inventario = root.Listbox(self)
        self.lista_inventario.pac
                    

## ? VENDAS

## TODO adicionar vendas de inventário de terceiros

    def submit_vendas(self): 
        db = sqlite3.connect('adm.db')
        cursor_db = db.cursor()

        cursor_db.execute("INSERT INTO vendas_table (data, categoria, valor) VALUES (:v_data, :v_categoria, :v_valor)",
            {
                "v_data": self.v_data.get(),
                "v_categoria": self.v_categoria.get(),
                "v_valor": self.v_valor.get()
            })

        db.commit()
        cursor_db.close()
        db.close()

        self.v_id.delete(0, END)
        self.v_data.delete(0, END)
        self.v_categoria.delete(0, END)
        self.v_valor.delete(0, END)

        self.lista_vendas.delete(*self.lista_vendas.get_children())
        self.mostrar_lista_vendas()

    def mostrar_lista_vendas(self):
        
        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute("SELECT * FROM vendas_table")
        data = cursor_db.fetchall()
        global count
        count = 0
        for row in data:
            if count % 2 == 0:
                self.lista_vendas.insert(parent = '', index ='end', iid=count, text = '', values=(row[0], row[1], row[2], row[3]), tags=('evenrow'))
            else:
                self.lista_vendas.insert(parent = '', index ='end', iid=count, text = '', values=(row[0], row[1], row[2], row[3]), tags=('oddrow'))
            count += 1

        cursor_db.close()
        new_db.commit()
        new_db.close()  

    def cleaning_vendas(self):
        self.v_id.delete(0, END)
        self.v_data.delete(0, END)
        self.v_categoria.delete(0, END)
        self.v_valor.delete(0, END)
    
    def select_entry_vendas(self, e):
        self.v_id.delete(0, END)
        self.v_data.delete(0, END)
        self.v_categoria.delete(0, END)
        self.v_valor.delete(0, END)

        selected = self.lista_vendas.focus()
        values = self.lista_vendas.item(selected, 'values')

        self.v_id.insert(0, values[0])
        self.v_data.insert(0, values[1])
        self.v_categoria.insert(0, values[2])
        self.v_valor.insert(0, values[3])

    def data_remove_vendas(self):
        selected = self.lista_vendas.selection()
        if not selected:
            return

        item = self.lista_vendas.item(selected)
        values = item['values']

        connection = sqlite3.connect("adm.db")
        cursor = connection.cursor()
        query = "DELETE FROM vendas_table WHERE id = ? AND data = ? AND categoria = ? AND valor = ? "
        cursor.execute(query, values)

        cursor.close()
        connection.commit()
        connection.close()

        self.lista_vendas.delete(selected)

    def update_vendas(self):
        selected = self.lista_vendas.focus()
        self.lista_vendas.item(selected, text = '', values = (self.v_id.get(), self.v_data.get(), self.v_categoria.get(), self.v_valor.get()))

        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute("""UPDATE vendas_table SET
            data = :data,
            categoria = :categoria,
            valor = :valor
        WHERE oid = :oid""", 
        {
            'data': self.v_data.get(),
            'categoria': self.v_categoria.get(),
            'valor': self.v_valor.get(),
            'oid':self.v_id.get()
        })

        new_db.commit()
        cursor_db.close()
        new_db.close()  

## ? INVENTARIOS
    def submit_inventario(self, type):
        db = sqlite3.connect('adm.db')
        cursor_db = db.cursor()

        table = ''
        inv = self.lista_inventario
        if type == 0:
            table = 'inventario_movel'
        elif type == 1:
            table = 'inventario_fixo'
            
        self.categoria_inv = self.i_selected_categoria.get()
        cursor_db.execute(f"INSERT INTO {table} (nome, valor, unidades, date) VALUES (:i_nome, :i_valor, :i_unidades, :i_data)",
                        {
                            "i_nome": self.i_nome.get(),
                            "i_valor": self.i_valor.get(),
                            "i_unidades": self.i_unidades.get(),
                            "i_data":self.i_data.get()
                        })
            
        db.commit()
        cursor_db.close()
        db.close()

        self.i_nome.delete(0, END)
        self.i_unidades.delete(0, END)
        self.i_categoria.set('')
        self.i_valor.delete(0, END)
        self.i_data.delete(0, END)
        self.mostrar_lista_inventario()

    def select_entry_inventario(self, e):
        self.i_nome.delete(0, END)
        self.i_categoria.set('')
        self.i_valor.delete(0, END)
        self.i_unidades.delete(0, END)
        self.i_data.delete(0, END)
        
        if self.current_tab_i == 0:
            self.i_categoria.set('Movel')
        if self.current_tab_i == 1:
            self.i_categoria.set('Fixo')
        if self.current_tab_i == 2:
            self.i_categoria.set('Perdido')

        selected = self.lista_inventario.focus()
        values = self.lista_inventario.item(selected, 'values')
        
        self.i_id_text.set(values[0])
        self.i_nome.insert(0, values[1])
        self.i_valor.insert(0, values[2])
        self.i_unidades.insert(0, values[3]) 
        self.i_data.insert(0, values[4]) 

    def cleaning_inventario(self):
        self.i_id_text.set('')
        self.i_nome.delete(0, END)
        self.i_unidades.delete(0, END)
        self.i_categoria.set('')
        self.i_valor.delete(0, END)
        self.i_data.delete(0, END)

    def mostrar_lista_inventario(self):
        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()            
        table = ''

        if self.current_tab_i == 0:
            table = 'inventario_movel'
        elif self.current_tab_i ==  1:
            table = 'inventario_fixo'
        elif self.current_tab_i == 2:
            table = 'inventario_perdido'

        self.lista_inventario.delete(*self.lista_inventario.get_children())

        cursor_db.execute(f"SELECT * FROM {table}")
                
        data = cursor_db.fetchall()

        global count
        count = 1
        self.lista_inventario.tag_configure('oddrow', background="white")
        self.lista_inventario.tag_configure('evenrow', background="lightblue")  
        
        if table == 'inventario_perdido':
            zero = ''
            for row in data:
                if count % 2 == 0:
                    self.lista_inventario.insert(parent = '', index ='end', text = '', values=(row[1], row[2], zero, row[3], row[4]), tags=('evenrow'))
                else:
                    self.lista_inventario.insert(parent = '', index ='end', text = '', values=(row[1], row[2], zero, row[3], row[4]), tags=('oddrow'))
                count += 1
        else:
            for row in data:
                if count % 2 == 0:
                    self.lista_inventario.insert(parent = '', index ='end', text = '', values=(row[0], row[1], row[2], row[3], row[4]), tags=('evenrow'))
                else:
                    self.lista_inventario.insert(parent = '', index ='end', text = '', values=(row[0], row[1], row[2], row[3], row[4]), tags=('oddrow'))
                count += 1

        cursor_db.close()
        new_db.commit()
        new_db.close()  

    def data_remove_inventario(self):

        table = ''
        item = ''
        selected = ''
        if self.current_tab_i == 0:
            table = 'inventario_movel'
            selected = self.lista_inventario.selection()
            item = self.lista_inventario.item(selected)
        elif self.current_tab_i == 1:
            table = 'inventario_fixo'
            selected = self.lista_inventario.selection()
            item = self.lista_inventario.item(selected)
        elif self.current_tab_i == 2:
            table = 'inventario_perdido'
            selected = self.lista_inventario.selection()
            item = self.lista_inventario.item(selected)
            
        
        values = item['values']
        valuesperdido = values[:2] + values[-2:]
        print(values)
        connection = sqlite3.connect("adm.db")
        cursor = connection.cursor()
        if self.current_tab_i != 2:
            cursor.execute(f"DELETE FROM {table} WHERE id = ? AND nome = ? AND valor = ? AND unidades = ? AND date = ? ", values)
        else:
            cursor.execute(f"DELETE FROM {table} WHERE inventario_id = ? AND nome = ? AND unidades = ? AND data = ? ", valuesperdido)
        cursor.close()
        connection.commit()
        connection.close()

        self.i_id_text.set('')
        self.i_nome.delete(0, END)
        self.i_unidades.delete(0, END)
        self.i_categoria.set('')
        self.i_valor.delete(0, END)
        self.i_data.delete(0, END)

        self.mostrar_lista_inventario()
    
## TODO ADD UPDATE TO INVENTARIO_PERDIDO
    def update_inventario(self):
        selected = ''
        table = ''
        if self.current_tab_i == 0:
            table = 'inventario_movel'
        if self.current_tab_i == 1:
            table = 'inventario_fixo'  
        if self.current_tab_i == 2:
            table = 'inventario_perdido'  

        selected = self.lista_inventario.focus()
        self.lista_inventario.item(selected, text = '', values = (self.i_id_text.get(), self.i_nome.get(), self.i_unidades.get(), self.i_valor.get(), self.i_data.get()))
        
        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute(f"""UPDATE {table} SET
            nome = :nome,
            unidades = :unidades,
            valor = :valor
            date = :date

        WHERE oid = :oid""", 
        {
            'nome': self.i_nome.get(),
            'unidades': self.i_unidades.get(),
            'valor': self.i_valor.get(),
            'oid':self.i_id_text.get(),
            'date':self.i_data.get()
        })

        new_db.commit()
        cursor_db.close()
        new_db.close() 
    
    def update_current_tab_i(self, event):
        self.current_tab_i = self.nb_inventario.index(self.nb_inventario.select())
        self.mostrar_lista_inventario()
        self.cleaning_inventario()
        
    def mostrar_lista_inventario_movel(self):
        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        self.lista_inventario.delete(*self.lista_inventario.get_children())

        cursor_db.execute("SELECT * FROM inventario_movel")        
        data = cursor_db.fetchall()
        self.lista_inventario.tag_configure('oddrow', background="white")
        self.lista_inventario.tag_configure('evenrow', background="lightblue")  
        global count
        count = 1
        for row in data:
            if count % 2 == 0:
                self.lista_inventario.insert(parent = '', index ='end', text = '', values=(row[0], row[1], row[2], row[3], row[4]), tags=('evenrow'))
            else:
                self.lista_inventario.insert(parent = '', index ='end', text = '', values=(row[0], row[1], row[2], row[3], row[4]), tags=('oddrow'))
            count += 1

        cursor_db.close()
        new_db.commit()
        new_db.close()  

    def select_entry_inventario_perdido(self, e):
        self.i_p_unidades.delete(0, END)
        self.i_p_data.delete(0, END)

        selected = self.lista_inventario.focus()
        values = self.lista_inventario.item(selected, 'values')
        
        self.i_p_id_var.set(values[0])
        self.i_p_nome_var.set(values[1])


## TODO pop-up de erro
    def submit_inventario_perdido(self):
        db = sqlite3.connect('adm.db')
        cursor_db = db.cursor()

        nome = self.i_p_nome_var.get()
        id = int(self.i_p_id_var.get())
        unidades_perdidas = int(self.i_p_unidades.get())
        data = self.i_p_data.get()

        cursor_db.execute('SELECT unidades FROM inventario_movel WHERE id = ?', (id,))
        unidades_atuais = cursor_db.fetchone()[0]

        if unidades_perdidas <= unidades_atuais:
            valor_atualizado = unidades_atuais - unidades_perdidas
            cursor_db.execute('UPDATE inventario_movel SET unidades = ? WHERE id = ?', (valor_atualizado, id))

            cursor_db.execute('INSERT INTO inventario_perdido (inventario_id, nome, unidades, data) VALUES (?, ?, ?, ?)',
                        (id, nome, unidades_perdidas, data))
            db.commit()
            #print(f'{lost_quantity} cup(s) removed from inventario_movel and added to lost_items.')
        #else:
            #print('Invalid quantity. The quantity of lost items cannot exceed the current quantity in inventario_movel.')

        # Close the database connection
        db.close()
        self.mostrar_lista_inventario_movel()

    def valor_total_item_inventario(self):
        ...

## ? CUSTOS E DESPESAS

    def submit_cd(self, type):
        
        if type == 0:
            table = 'custos'
        elif type == 1:
            table = 'despesas'
        else:
            return
        
        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute('INSERT INTO custos_despesas (nome, valor, data, categoria) VALUES (:cd_nome, :cd_valor, :cd_data, :cd_categoria)',
        {
            "cd_nome":self.cd_nome.get(),
            "cd_valor":self.cd_valor.get(),
            "cd_data":self.cd_data.get(),
            "cd_categoria":self.cd_categoria.get()
        })

        cursor_db.execute(f'INSERT INTO {table} (nome, valor, data) VALUES (:cd_nome, :cd_valor, :cd_data)',
        {
            "cd_nome":self.cd_nome.get(),
            "cd_valor":self.cd_valor.get(),
            "cd_data":self.cd_data.get(),
        })

        new_db.commit()
        cursor_db.close()
        new_db.close()

        
        self.cd_id.delete(0, END)
        self.cd_nome.delete(0, END)
        self.cd_valor.delete(0, END)
        self.cd_data.delete(0, END)
        self.cd_categoria.set('')

        self.lista_cd.delete(*self.lista_cd.get_children())
        self.mostrar_lista_cd()

    def select_cd(self, e):
        self.cd_id.delete(0, END)
        self.cd_nome.delete(0, END)
        self.cd_valor.delete(0, END)
        self.cd_data.delete(0, END)
        self.cd_categoria.set('')

        selected = self.lista_cd.focus()

        values = self.lista_cd.item(selected, 'values')

        self.cd_id.insert(0, values[0])
        self.cd_nome.insert(0, values[1])
        self.cd_valor.insert(0, values[2])
        self.cd_data.insert(0, values[3])
        self.cd_categoria.set(values[4])

    def cleaning_cd(self):
        self.cd_id.delete(0, END)
        self.cd_nome.delete(0, END)
        self.cd_valor.delete(0, END)
        self.cd_data.delete(0, END)
        self.cd_categoria.set('')
    
    def mostrar_lista_cd(self):
        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute("SELECT * FROM custos_despesas")
        data = cursor_db.fetchall()
        for row in data:
            self.lista_cd.insert(parent = '', index = 'end', text = '', values=(row[0], row[1], row[2], row[3], row[4]))
   
        cursor_db.close()
        new_db.commit()
        new_db.close()

## ! VER DEPOIS SE ISSO N BUGA
    def data_remove_cd(self):
        selected = self.lista_cd.selection()
        if not selected:
            return 

        table = ''
        values2=[]
        item = self.lista_cd.item(selected)
        values = item['values']
        if values[4] == 'Custo':
            table = 'custos'
            values2 = values[1], values[2], values[3]
        if values[4] == 'Despesa':
            table = 'despesas'
            values2 = values[1], values[2], values[3]
        
        connection = sqlite3.connect("adm.db")
        cursor = connection.cursor()
        
        query = "DELETE FROM custos_despesas WHERE id = ? AND nome = ? AND valor = ? AND data = ? AND categoria = ? "
        cursor.execute(query, values)
        query = f'DELETE FROM {table} WHERE nome = ? AND valor = ? AND data = ?'
        cursor.execute(query, values2)

    
        cursor.close()
        connection.commit()
        connection.close()

        self.lista_cd.delete(selected)

## TODO ATUALIZAR OS VALORES DAS LISTAS ISOLADAS A PARTIR DAQUI TBM
    def update_cd(self):
        selected = self.lista_cd.focus()
        self.lista_cd.item(selected, text = '', values = (self.cd_id.get(),self.cd_nome.get(), self.cd_valor.get(), self.cd_data.get(), self.cd_categoria.get()))

        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute("""UPDATE custos_despesas SET
            nome = :nome,
            valor = :valor,
            data = :data,
            categoria = :categoria

        WHERE oid = :oid""", 
        {
            'oid':self.cd_id.get(),
            'nome':self.cd_nome.get(),
            'valor': self.cd_valor.get(),
            'data': self.cd_data.get(),
            'categoria': self.cd_categoria.get()
        })

        new_db.commit()
        cursor_db.close()
        new_db.close()  

    def lista_ind_cd(self):
        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute("SELECT * FROM custos")
        data = cursor_db.fetchall()
        for row in data:
            self.lista_c.insert(parent = '', index = 'end', text = '', values=(row[0], row[1], row[2], row[3]))
   
        cursor_db.close()
        new_db.commit()
        new_db.close()

        new_db = sqlite3.connect('adm.db')
        cursor_db = new_db.cursor()

        cursor_db.execute("SELECT * FROM despesas")
        data = cursor_db.fetchall()
        for row in data:
            self.lista_d.insert(parent = '', index = 'end', text = '', values=(row[0], row[1], row[2], row[3]))
   
## // lembrar de remover tambem das listas isoladas de custos e despesas caso remova da lista geral
        cursor_db.close()
        new_db.commit()
        new_db.close()

## ? Relatorios

## TODO tenho que fazer pela semana

    def lista_semanal_pe(self):
        self.lista_diaria.delete(*self.lista_diaria.get_children())
        new_db = sqlite3.connect('adm.db')
        cursor = new_db.cursor()

        month = self.sel_mes_diario.get()
        if len(month) == 1:
            month = '0' + month

        cursor.execute("SELECT substr(data, 1, 2), SUM(valor) FROM custos WHERE substr(data, 4, 2) = ? GROUP BY substr(data, 1, 2)", (month,))
        valor_custo = cursor.fetchall()

        cursor.execute("SELECT substr(data, 1, 2), SUM(valor) FROM vendas_table WHERE substr(data, 4, 2) = ? GROUP BY substr(data, 1, 2)", (month,))
        valor_vendas = cursor.fetchall()

        lista_d = {'dia': None, 'valor_recebido': None, 'valor_gasto': None, 'diferença': None}
        result = []

        for row in valor_vendas:
            dia = row[0]
            valor_recebido = row[1]
            lista_d = {'dia': dia, 'valor_recebido': valor_recebido, 'valor_gasto': None, 'diferença': None}
            result.append(lista_d)

        for row in valor_custo:
            dia = row[0]
            valor_gasto = row[1]
            for item in result:
                if item['dia'] == dia:
                    item['valor_gasto'] = valor_gasto
                    break

        for item in result:
            if item['valor_gasto'] == None:
                item['valor_gasto'] = 0
            elif item['valor_recebido'] == None:
                item['valor_recebido'] = 0
            item['diferença'] = float(item['valor_recebido']) - float(item['valor_gasto'])
            
        for row in result:
            dia = row['dia']
            valor_recebido = row['valor_recebido']
            valor_gasto = row['valor_gasto']
            diferença = row['diferença']
            self.lista_diaria.insert(parent='', index='end', text='', values=(dia, valor_recebido, valor_gasto, diferença))

        cursor.close()
        new_db.close()

    def lista_diario_pe(self):
        self.lista_diaria.delete(*self.lista_diaria.get_children())
        new_db = sqlite3.connect('adm.db')
        cursor = new_db.cursor()

        month = self.sel_mes_diario.get()
        if len(month) == 1:
            month = '0' + month

        cursor.execute("SELECT substr(data, 1, 2), SUM(valor) FROM custos WHERE substr(data, 4, 2) = ? GROUP BY substr(data, 1, 2)", (month,))
        valor_custo = cursor.fetchall()

        cursor.execute("SELECT substr(data, 1, 2), SUM(valor) FROM vendas_table WHERE substr(data, 4, 2) = ? GROUP BY substr(data, 1, 2)", (month,))
        valor_vendas = cursor.fetchall()

        lista_d = {'dia': None, 'valor_recebido': None, 'valor_gasto': None, 'diferença': None}
        result = []

        for row in valor_vendas:
            dia = row[0]
            valor_recebido = row[1]
            lista_d = {'dia': dia, 'valor_recebido': valor_recebido, 'valor_gasto': None, 'diferença': None}
            result.append(lista_d)

        for row in valor_custo:
            dia = row[0]
            valor_gasto = row[1]
            for item in result:
                if item['dia'] == dia:
                    item['valor_gasto'] = valor_gasto
                    break

        for item in result:
            if item['valor_gasto'] == None:
                item['valor_gasto'] = 0
            elif item['valor_recebido'] == None:
                item['valor_recebido'] = 0
            item['diferença'] = float(item['valor_recebido']) - float(item['valor_gasto'])
            
        for row in result:
            dia = row['dia']
            valor_recebido = row['valor_recebido']
            valor_gasto = row['valor_gasto']
            diferença = row['diferença']
            self.lista_diaria.insert(parent='', index='end', text='', values=(dia, valor_recebido, valor_gasto, diferença))



        cursor.close()
        new_db.close()

    def lista_ponto_eq(self):

        self.lista_pe.delete(*self.lista_pe.get_children())
        new_db = sqlite3.connect('adm.db')
        cursor = new_db.cursor()

        days = 0
        month = self.sel_mes_pe.get()
        if len(month) == 1:
            month = '0' + month
        if month == '01' or '03' or '05' or '07' or '08' or '10' or '12':
            days = 31
        elif month == '04' or '06' or '09' or '11':
            days = 30
        else:
            days = 29


        cursor.execute("SELECT substr(data, 1, 2), SUM (valor) FROM despesas WHERE substr(data, 4, 2) = ? GROUP BY substr(data, 1, 2)", (month,))
        valor_despesa = cursor.fetchall()
        cursor.execute("SELECT substr(data, 1, 2), SUM(valor) FROM custos WHERE substr(data, 4, 2) = ? GROUP BY substr(data, 1, 2)", (month,))
        valor_custo = cursor.fetchall()
        cursor.execute("SELECT substr(data, 1, 2), SUM(valor) FROM vendas_table WHERE substr(data, 4, 2) = ? GROUP BY substr(data, 1, 2)", (month,))
        valor_vendas = cursor.fetchall()


        lista_d = {'dia': None, 'valor_recebido': None, 'valor_gasto_custo':None, 'valor_gasto_despesa':None, 'diferença': None}
        result = []
        diferença_dia = 0

        for row in valor_vendas:
            dia = row[0]
            valor_recebido = row[1]
            lista_d = {'dia': dia, 'valor_recebido': valor_recebido}
            result.append(lista_d)

        for row in valor_custo:
            dia = row[0]
            valor_custo = row[1]
            lista_d = {'dia': dia, 'valor_gasto_custo': valor_custo}
            result.append(lista_d)

        for row in valor_despesa:
            dia = row[0]
            valor_despesa = row[1]
            lista_d = {'dia': dia, 'valor_gasto_despesa': valor_despesa}
            result.append(lista_d)

        dados_dia = {}

        for row in result:
            dia = row['dia']
            valor_recebido = row.get('valor_recebido')
            valor_gasto_custo = row.get('valor_gasto_custo')
            valor_gasto_despesa = row.get('valor_gasto_despesa')
            
            if dia in dados_dia:
                if valor_recebido != None:
                    dados_dia[dia]['valor_recebido'] = valor_recebido
                if valor_gasto_custo != None:
                    dados_dia[dia]['valor_gasto_custo'] = valor_gasto_custo
                if valor_gasto_despesa != None:
                    dados_dia[dia]['valor_gasto_despesa'] = valor_gasto_despesa
            else:
                dados_dia[dia] = {'valor_recebido': valor_recebido, 'valor_gasto_custo': valor_gasto_custo, 'valor_gasto_despesa':valor_gasto_despesa}


        lista_final = {'dia': None, 'valor_recebido': None, 'valor_gasto':None, 'diferença': None}
        lista_final_resultados = []

        for row in dados_dia:
            dia = row[0]+row[1]
            if dados_dia[dia]['valor_recebido'] == None:
                valor_recebido = dados_dia[dia]['valor_recebido'] = 0
            valor_recebido = dados_dia[dia]['valor_recebido']
            if dados_dia[dia]['valor_gasto_custo'] == None:
                dados_dia[dia]['valor_gasto_custo'] = 0
            if dados_dia[dia]['valor_gasto_despesa'] == None:
                dados_dia[dia]['valor_gasto_despesa'] = 0
            valor_gasto = dados_dia[dia]['valor_gasto_custo'] + dados_dia[dia]['valor_gasto_despesa']
            diferença = valor_recebido - valor_gasto
            lista_final = {'dia': dia, 'valor_recebido':valor_recebido, 'valor_gasto':valor_gasto, 'diferença':diferença}
            lista_final_resultados.append(lista_final)

        

        for row in lista_final_resultados:
            dia = row['dia']
            valor_recebido = row['valor_recebido']
            valor_gasto = row['valor_gasto']
            diferença = row['diferença']
            if diferença_dia == 0:
                diferença_dia = valor_recebido - valor_gasto
            elif diferença_dia > 0:
                diferença_dia = diferença_dia + valor_recebido - valor_gasto
            elif diferença_dia < 0:
                diferença_dia = valor_recebido - diferença_dia - valor_gasto
            self.lista_pe.insert(parent='', index='end', text='', values=(dia, valor_recebido, valor_gasto, diferença, diferença_dia))


        
class App(Funcs):
    def __init__(self):
        self.pe_valor_mes = ''
        self.pe_saldo_mes = ''
        self.root = root
        self.screen()
        self.current_tab_i = 0
        self.select_screen('tela_relatorios')
        self.center_window(self.root)
        root.mainloop()

    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x_offset = (window.winfo_screenwidth() - width) // 2
        y_offset = (window.winfo_screenheight() - height) // 2
        window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    def screen(self):
        self.root.title("ADM")
        self.root.configure(background = '#7d0c87')
        self.root.geometry('1000x600')
        self.root.resizable(True, True)

    def select_screen(self, screen_name):  
        self.clean_screen()
        if screen_name == 'tela_inicial':
            self.tela_inicial()
            self.root.title('APP')
        elif screen_name == 'tela_inventario':
            self.tela_inventario()
            self.root.title('Inventário')
            self.mostrar_lista_inventario()
        elif screen_name == 'tela_estoque':
            self.tela_estoque()
            self.root.title('Estoque')
        elif screen_name == 'tela_vendas':
            self.tela_vendas()
            self.root.title('Vendas')
            self.mostrar_lista_vendas()
        elif screen_name == 'tela_vendas_terceiras':
            self.tela_vendas_terceiras()
            self.root.title('Vendas Terceiras')
        elif screen_name == 'tela_custos_despesas':
            self.tela_custos_despesas()
            self.root.title('Custos e Despesas')
            self.mostrar_lista_cd()
        elif screen_name == 'tela_relatorios':
            self.tela_relatorios()
            self.root.title('Relatórios')
        elif screen_name == 'tela_diario':
            self.tela_diario()
            self.root.title('Relatório Diário')
        elif screen_name == "tela_semanal":
            self.tela_semanal()
            self.root.title('Relatório Semanal')
        elif screen_name == "tela_cd":
            self.root.title('Custos e Despesas Individual')
            self.tela_cd()
            self.lista_ind_cd()
        elif screen_name == 'tela_inventario_perdido':
            self.root.title('Remover do Inventário')
            self.tela_inventario_perdido()
            self.mostrar_lista_inventario_movel()

    def clean_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def button_callback(self, screen_name):
        self.select_screen(screen_name)

    def tela_inicial(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.45)
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_2.place(relx=0.01, rely = 0.45, relwidth=0.98, relheight=0.54)

        self.see_inventory = Button(self.frame_2, text = "Inventário", command=lambda: self.button_callback("tela_inventario"))
        self.see_inventory.place(relx= 0.06, rely = 0.1, relwidth=0.28, relheight=0.3)
        self.see_vendas = Button(self.frame_2, text = "Vendas", command=lambda: self.button_callback("tela_vendas"))
        self.see_vendas.place(relx= 0.36, rely = 0.1, relwidth=0.28, relheight=0.3)
        self.see_estoque = Button(self.frame_2, text = "Estoque", command=lambda: self.button_callback("tela_estoque"))
        self.see_estoque.place(relx= 0.66, rely = 0.1, relwidth=0.28, relheight=0.3)
        self.see_custos = Button(self.frame_2, text = "Custos e Despesas", command=lambda: self.button_callback("tela_custos_despesas"))
        self.see_custos.place(relx= 0.2, rely = 0.6, relwidth=0.29, relheight=0.3)
        self.see_relatorios = Button(self.frame_2, text = "Relatórios", command=lambda: self.button_callback("tela_relatorios"))
        self.see_relatorios.place(relx= 0.51, rely = 0.6, relwidth=0.29, relheight=0.3)
      
    def tela_inventario(self):
        self.nb_inventario = ttk.Notebook(self.root, width = 975, height = 350)
        self.frame_nb = Frame(self.nb_inventario, bd = 4, bg = '#000000')
        
        self.frame1nb = Frame(self.nb_inventario)
        self.frame1nb.pack(padx=5, pady=5)
        self.label1nb = Label(self.frame1nb, text = 'INVENTÁRIO MÓVEL')
        self.label1nb.pack(padx=5, pady=5)
        self.nb_inventario.add(self.frame1nb, text = 'INVENTÁRIO MÓVEL')

        self.frame2nb = Frame(self.nb_inventario)
        self.label2nb = Label(self.frame2nb, text = 'INVENTÁRIO FIXO')
        self.label2nb.pack(padx=5, pady=5)
        self.frame2nb.pack(padx=5, pady=5)
        self.nb_inventario.add(self.frame2nb, text = 'INVENTÁRIO FIXO')

        self.frame3nb = Frame(self.nb_inventario)
        self.label3nb = Label(self.frame3nb, text = 'INVENTÁRIO PERDIDO')
        self.label3nb.pack(padx=5, pady=5)
        self.frame3nb.pack(padx=5, pady=5)
        self.nb_inventario.add(self.frame3nb, text = 'INVENTÁRIO PERDIDO')
        self.nb_inventario.pack(padx = 5, pady = 5)
        
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 1)        
        self.frame_2.place(relx = 0.01, rely = 0.75, relwidth=0.98, relheight=0.24)
        self.frame_3 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 1)        
        self.frame_3.place(relx = 0.01, rely = 0.6, relwidth=0.98, relheight=0.15)        

        self.lista_inventario = ttk.Treeview(self.nb_inventario, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5'), selectmode = 'extended')
        self.lista_inventario.heading("#0", text = "")
        self.lista_inventario.heading("#1", text = "ID")
        self.lista_inventario.heading("#2", text = "Nome")
        self.lista_inventario.heading("#3", text = "Valor")
        self.lista_inventario.heading("#4", text = "Unidades")
        self.lista_inventario.heading("#5", text = "Data")

        self.lista_inventario.column("#0", width = 1)
        self.lista_inventario.column("#1", width = 25)
        self.lista_inventario.column("#2", width =100)
        self.lista_inventario.column("#3", width =75)
        self.lista_inventario.column("#4", width =75)
        self.lista_inventario.column("#5", width =175)

        self.lista_inventario.place(relx=0.001, rely=0.15, relwidth=0.965, relheight=0.79)

        self.scroll_lista = Scrollbar(self.frame1nb, orient='vertical')
        self.lista_inventario.configure(yscroll = self.scroll_lista.set)
        self.scroll_lista.place(relx=0.97, rely =0.1, relwidth=0.03, relheight = 0.8)
        self.scroll_lista2 = Scrollbar(self.frame2nb, orient='vertical')
        self.lista_inventario.configure(yscroll = self.scroll_lista2.set)
        self.scroll_lista2.place(relx=0.97, rely =0.1, relwidth=0.03, relheight = 0.8)
        self.scroll_lista3 = Scrollbar(self.frame3nb, orient='vertical')
        self.lista_inventario.configure(yscroll = self.scroll_lista3.set)
        self.scroll_lista3.place(relx=0.97, rely =0.1, relwidth=0.03, relheight = 0.8)

        self.i_id_text = IntVar()
        self.i_id = Label(self.frame_3, textvariable = self.i_id_text)
        self.i_id.place(relx = 0.02, rely = 0.4, relwidth = 0.05, relheight = 0.5)
        self.i_selected_categoria = StringVar()
        self.i_categoria = ttk.Combobox(self.frame_3, textvariable = self.i_selected_categoria, height = 10)
        self.i_categoria['values'] = ('Movel', 'Fixo')
        self.i_categoria['state'] = 'readonly'                        
        self.i_categoria.pack()
        self.categoria_i = self.i_selected_categoria.get()
        self.i_categoria.place(relx = 0.07, rely = 0.4, relwidth = 0.15, relheight = 0.5)
        self.i_nome = Entry(self.frame_3, text = 'Nome')
        self.i_nome.place(relx = 0.22, rely = 0.4, relwidth = 0.2, relheight = 0.5)
        self.i_valor = Entry(self.frame_3, text = 'Valor')
        self.i_valor.place(relx = 0.42, rely = 0.4, relwidth = 0.15, relheight = 0.5)
        self.i_unidades = Entry(self.frame_3, text = 'Unidades')
        self.i_unidades.place(relx = 0.57, rely = 0.4, relwidth = 0.1, relheight = 0.5)
        self.i_data = Entry(self.frame_3, text = 'DATA')
        self.i_data.place(relx=0.67, rely = 0.4, relwidth = 0.1, relheight = 0.5)

        self.nome_label_inv = Label(self.frame_3, text = "Nome")
        self.nome_label_inv.place(relx = 0.22, rely = 0.1, relwidth = 0.2, relheight = 0.3)
        self.categoria_label_inv = Label(self.frame_3, text = "Categoria")
        self.categoria_label_inv.place(relx = 0.07, rely = 0.1, relwidth = 0.15, relheight = 0.3)
        self.id_label_inv = Label(self.frame_3, text = "ID")
        self.id_label_inv.place(relx = 0.02, rely = 0.1, relwidth = 0.05, relheight = 0.3)
        self.valor_label_inv = Label(self.frame_3, text = "Valor")
        self.valor_label_inv.place(relx = 0.42, rely = 0.1, relwidth = 0.15, relheight = 0.3)
        self.unidades_label_inv = Label(self.frame_3, text = "Unidades")
        self.unidades_label_inv.place(relx = 0.57, rely = 0.1, relwidth = 0.1, relheight = 0.3)
        self.data_label_inv = Label(self.frame_3, text = "Data")
        self.data_label_inv.place(relx = 0.67, rely = 0.1, relwidth = 0.1, relheight = 0.3)

        self.adicionar_inventario = Button(self.frame_3, text = 'ADICIONAR AO INVENTÁRIO', command =lambda: self.submit_inventario(self.i_categoria.current()))
        self.adicionar_inventario.place(relx = 0.80, rely = 0.05, relwidth = 0.18, relheight = 0.9)
        
        self.voltar_tela = Button(self.frame_2, text = "VOLTAR", command=lambda: self.button_callback("tela_inicial"))
        self.voltar_tela.place(relx= 0.01, rely = 0.2, relwidth=0.15, relheight=0.6)
        self.limpar_inventario = Button(self.frame_2, text = 'Limpar', command = self.cleaning_inventario)
        self.limpar_inventario.place(relx= 0.21, rely = 0.1, relwidth=0.2, relheight=0.35)
        self.atualizar_inventario = Button(self.frame_2, text = 'UPDATE', command=self.update_inventario)
        self.atualizar_inventario.place(relx= 0.41, rely = 0.1, relwidth=0.2, relheight=0.35)
        self.deletar_inventario = Button(self.frame_2, text = 'DELETAR', command =self.data_remove_inventario)
        self.deletar_inventario.place(relx= 0.61, rely = 0.1, relwidth=0.2, relheight=0.35)
        self.add_perdido = Button(self.frame_2, text = 'REMOVER DO INVENTARIO MÓVEL', command=lambda:self.button_callback('tela_inventario_perdido'))
        self.add_perdido.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.5)

        self.lista_inventario.bind('<ButtonRelease-1>', self.select_entry_inventario)
        self.nb_inventario.bind("<<NotebookTabChanged>>", self.update_current_tab_i)

    def tela_estoque(self):

        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.77)
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_2.place(relx=0.01, rely = 0.77, relwidth=0.98, relheight=0.22)

        self.estoque_label = Label(self.frame_1, text = 'ESTOQUE')
        self.estoque_label.place(relx=0.4, rely= 0.005, relwidth=0.2, relheight=0.05)

        self.lista_estoque = ttk.Treeview(self.frame_1, height=3,  column=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'), selectmode = 'extended')
        self.lista_estoque.heading("#0", text = "")
        self.lista_estoque.heading("#1", text = "ID")
        self.lista_estoque.heading("#2", text = "Data")
        self.lista_estoque.heading("#3", text = "PRODUTO")
        self.lista_estoque.heading("#4", text = "Quantidade")
        self.lista_estoque.heading("#5", text = "Valor Un")
        self.lista_estoque.heading("#6", text = "Valor TOTAL")

        self.lista_estoque.column("#0", width = 1)
        self.lista_estoque.column("#1", width = 20)
        self.lista_estoque.column("#2", width = 100)
        self.lista_estoque.column("#3", width = 125)
        self.lista_estoque.column("#4", width = 50)
        self.lista_estoque.column("#5", width = 75)
        self.lista_estoque.column("#6", width = 100)

        self.lista_estoque.place(relx=0.02, rely=0.1, relheight=0.65, relwidth=0.94)

        self.scroll_lista = Scrollbar(self.frame_1, orient='vertical')
        self.lista_estoque.configure(yscroll = self.scroll_lista.set)
        self.scroll_lista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight = 0.65)

        self.voltar_tela = Button(self.frame_2, text = "VOLTAR", command=lambda: self.button_callback("tela_inicial"))
        self.voltar_tela.place(relx= 0.005, rely = 0.645, relwidth=0.2, relheight=0.35)

    def tela_vendas(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.005, relwidth=0.98, relheight=0.75)
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)        
        self.frame_2.place(relx = 0.01, rely = 0.75, relwidth=0.98, relheight=0.24)

        self.lista_vendas = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4'), selectmode = 'extended')
        self.lista_vendas.heading("#0", text = "")
        self.lista_vendas.heading("#1", text = "ID")
        self.lista_vendas.heading("#2", text = "Data")
        self.lista_vendas.heading("#3", text = "Categoria")
        self.lista_vendas.heading("#4", text = "Valor")

        self.lista_vendas.column("#0", width = 1)
        self.lista_vendas.column("#1", width = 25)
        self.lista_vendas.column("#2", width = 150)
        self.lista_vendas.column("#3", width =150)
        self.lista_vendas.column("#4", width =250)

        self.lista_vendas.place(relx=0.001, rely=0.1, relwidth=0.975, relheight=0.65)

        self.scroll_lista = Scrollbar(self.frame_1, orient='vertical')
        self.lista_vendas.configure(yscroll = self.scroll_lista.set)
        self.scroll_lista.place(relx=0.97, rely =0.1, relwidth=0.03, relheight = 0.65)

        self.v_label = Label(self.frame_1, text = 'VENDAS DA LOJA')
        self.v_label.place(relx=0.4, rely=0.01, relwidth = 0.2, relheight=0.08)

        self.v_id = Entry(self.frame_1, text = 'id')
        self.v_id.place(relx = 0.02, rely = 0.87, relwidth = 0.1, relheight = 0.1)
        self.v_data = Entry(self.frame_1, text = 'DATA')
        self.v_data.place(relx = 0.12, rely = 0.87, relwidth = 0.2, relheight = 0.1)
        self.v_categoria = Entry(self.frame_1, text = 'CATEGORIA')
        self.v_categoria.place(relx = 0.32, rely = 0.87, relwidth = 0.2, relheight = 0.1)
        self.v_valor = Entry(self.frame_1, text = 'Valor')
        self.v_valor.place(relx = 0.52, rely = 0.87, relwidth = 0.2, relheight = 0.1)

        self.id_label_vendas = Label(self.frame_1, text = "ID")
        self.id_label_vendas.place(relx = 0.02, rely = 0.77, relwidth = 0.1, relheight = 0.1)
        self.data_label_vendas = Label(self.frame_1, text = "DATA")
        self.data_label_vendas.place(relx = 0.12, rely = 0.77, relwidth = 0.2, relheight = 0.1)
        self.categoria_label_vendas = Label(self.frame_1, text = "??CATEGORIA??")
        self.categoria_label_vendas.place(relx = 0.32, rely = 0.77, relwidth = 0.2, relheight = 0.1)
        self.valor_label_vendas = Label(self.frame_1, text = "VALOR")
        self.valor_label_vendas.place(relx = 0.52, rely = 0.77, relwidth = 0.2, relheight = 0.1)

        self.voltar_tela = Button(self.frame_2, text = "VOLTAR", command=lambda: self.button_callback("tela_inicial"))
        self.voltar_tela.place(relx= 0.01, rely = 0.25, relwidth=0.15, relheight=0.6)
        self.vendas_t_tela = Button(self.frame_2, text = "VENDAS TERCEIRAS", command=lambda: self.button_callback("tela_vendas_terceiras"))
        self.vendas_t_tela.place(relx= 0.84, rely = 0.25, relwidth=0.15, relheight=0.6)

        self.add_button = Button (self.frame_1, text = 'ADICIONAR DADO', command = self.submit_vendas)
        self.add_button.place(relx=0.76, rely =0.79, relwidth=0.2, relheight = 0.17)
        self.update_button = Button (self.frame_2, text = 'ATUALIZAR', command = self.update_vendas)
        self.update_button.place(relx=0.2, rely =0.005, relwidth=0.2, relheight = 0.5)
        self.rmv_button = Button (self.frame_2, text = 'REMOVER', command = self.data_remove_vendas)
        self.rmv_button.place(relx=0.4, rely =0.005, relwidth=0.2, relheight = 0.5)
        self.clear_button = Button (self.frame_2, text = 'LIMPAR ESPAÇOS', command = self.cleaning_vendas)
        self.clear_button.place(relx=0.6, rely =0.005, relwidth=0.2, relheight = 0.5)

        self.lista_vendas.bind('<ButtonRelease-1>', self.select_entry_vendas)

    def tela_inventario_perdido(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.77)
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_2.place(relx=0.01, rely = 0.77, relwidth=0.98, relheight=0.22)

        self.lista_inventario = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5'), selectmode = 'extended')
        self.lista_inventario.heading("#0", text = "")
        self.lista_inventario.heading("#1", text = "ID")
        self.lista_inventario.heading("#2", text = "Nome")
        self.lista_inventario.heading("#3", text = "Valor")
        self.lista_inventario.heading("#4", text = "Unidades")
        self.lista_inventario.heading("#5", text = "Data")

        self.lista_inventario.column("#0", width = 1)
        self.lista_inventario.column("#1", width = 25)
        self.lista_inventario.column("#2", width =100)
        self.lista_inventario.column("#3", width =75)
        self.lista_inventario.column("#4", width =75)
        self.lista_inventario.column("#5", width =175)

        self.lista_inventario.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.7)
        
        self.i_p_id_label = Label(self.frame_1, text = 'ID')
        self.i_p_id_label.place(relx=0.05, rely=0.8, relwidth=0.1, relheight=0.08)
        self.i_p_nome_label = Label(self.frame_1, text = 'Nome')
        self.i_p_nome_label.place(relx=0.15, rely=0.8, relwidth=0.2, relheight=0.08)
        self.i_p_unidades_label = Label(self.frame_1, text = 'Unidades Perdidas')
        self.i_p_unidades_label.place(relx=0.35, rely=0.8, relwidth=0.15, relheight=0.08)
        self.i_p_data_label = Label(self.frame_1, text = 'Data da Perda')
        self.i_p_data_label.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.08)

        self.i_p_id_var = IntVar()
        self.i_p_id = Label(self.frame_1, textvariable = self.i_p_id_var)
        self.i_p_id.place(relx=0.05, rely=0.88, relwidth=0.1, relheight=0.1)
        self.i_p_nome_var = StringVar()
        self.i_p_nome = Label(self.frame_1, textvariable = self.i_p_nome_var)
        self.i_p_nome.place(relx=0.15, rely=0.88, relwidth=0.2, relheight=0.1)

        self.i_p_unidades = Entry(self.frame_1, text = 'Unidades')
        self.i_p_unidades.place(relx = 0.35, rely = 0.88, relwidth = 0.15, relheight = 0.1)
        self.i_p_data = Entry(self.frame_1, text = 'DATA')
        self.i_p_data.place(relx=0.5, rely = 0.88, relwidth = 0.2, relheight = 0.1)
        
        self.voltar_tela = Button(self.frame_2, text = "VOLTAR", command=lambda: self.button_callback("tela_inventario"))
        self.voltar_tela.place(relx= 0.01, rely = 0.2, relwidth=0.15, relheight=0.6)
        self.remover_inventario = Button(self.frame_1, text = 'REMOVER DO INVENTARIO', command=self.submit_inventario_perdido)
        self.remover_inventario.place(relx=0.75, rely=0.82, relwidth=0.2, relheight=0.15)

        self.lista_inventario.bind('<ButtonRelease-1>', self.select_entry_inventario_perdido)



## TODO editar dados aqui e criar calculos, além da table e formatar disposição
    def tela_vendas_terceiras(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 4)
        self.frame_1.place(relx=0.02, rely = 0.05, relwidth=0.90, relheight=0.7)
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 4)        
        self.frame_2.place(relx = 0.02, rely = 0.80, relwidth=0.96, relheight=0.18)

        self.voltar_tela = Button(self.frame_2, text = "VOLTAR", command=lambda: self.button_callback("tela_vendas"))
        self.voltar_tela.place(relx= 0.05, rely = 0.5, relwidth=0.2, relheight=0.5)

        self.v_id = Entry(self.frame_1, text = 'id')
        self.v_id.place(relx = 0.02, rely = 0.82, relwidth = 0.1, relheight = 0.1)
        self.v_data = Entry(self.frame_1, text = 'DATA')
        self.v_data.place(relx = 0.12, rely = 0.82, relwidth = 0.1, relheight = 0.1)
        self.v_nome = Entry(self.frame_1, text = 'Nome')
        self.v_nome.place(relx=0.22, rely=0.82, relwidth=0.2, relheight=0.1)
        self.v_valor_total = Entry(self.frame_1, text = 'Valor Total')
        self.v_valor_total.place(relx = 0.42, rely = 0.82, relwidth = 0.15, relheight = 0.1)
        self.v_valor_recebido = Entry(self.frame_1, text = 'Valor Recebido')
        self.v_valor_recebido.place(relx = 0.57, rely = 0.82, relwidth = 0.15, relheight = 0.1)

        self.id_label_vendas = Label(self.frame_1, text = "ID")
        self.id_label_vendas.place(relx = 0.02, rely = 0.72, relwidth = 0.1, relheight = 0.1)
        self.data_label_vendas = Label(self.frame_1, text = "Data")
        self.data_label_vendas.place(relx = 0.12, rely = 0.72, relwidth = 0.1, relheight = 0.1)
        self.v_nome = Label(self.frame_1, text = 'Nome')
        self.v_nome.place(relx=0.22, rely=0.72, relwidth=0.2, relheight=0.1)
        self.valor_total_label_vendas = Label(self.frame_1, text = "Valor Total")
        self.valor_total_label_vendas.place(relx = 0.42, rely = 0.72, relwidth = 0.15, relheight = 0.1)
        self.valor_recebido_label_vendas = Label(self.frame_1, text = "Valor Recebido")
        self.valor_recebido_label_vendas.place(relx = 0.57, rely = 0.72, relwidth = 0.15, relheight = 0.1)

        self.lista_vendas = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5'), selectmode = 'extended')
        self.lista_vendas.heading("#0", text = "")
        self.lista_vendas.heading("#1", text = "ID")
        self.lista_vendas.heading("#2", text = "Data")
        self.lista_vendas.heading("#3", text = "Nome")
        self.lista_vendas.heading("#4", text = "Valor Total")
        self.lista_vendas.heading("#5", text = "Valor Recebido")

        self.lista_vendas.column("#0", width = 1)
        self.lista_vendas.column("#1", width = 75)
        self.lista_vendas.column("#2", width = 75)
        self.lista_vendas.column("#3", width =200)
        self.lista_vendas.column("#4", width =200)
        self.lista_vendas.column("#5", width =200)

        self.lista_vendas.place(relx=0.001, rely=0.005, relwidth=0.975, relheight=0.65)

        self.scroll_lista = Scrollbar(self.frame_1, orient='vertical')
        self.lista_vendas.configure(yscroll = self.scroll_lista.set)
        self.scroll_lista.place(relx=0.97, rely =0.005, relwidth=0.03, relheight = 0.65)

        self.add_button = Button (self.frame_1, text = 'ADICIONAR DADO', command = self.submit_vendas)
        self.add_button.place(relx=0.76, rely =0.74, relwidth=0.2, relheight = 0.17)
        self.update_button = Button (self.frame_2, text = 'ATUALIZAR', command = self.update_vendas)
        self.update_button.place(relx=0.34, rely =0.005, relwidth=0.2, relheight = 0.3)
        self.rmv_button = Button (self.frame_2, text = 'REMOVER', command = self.data_remove_vendas)
        self.rmv_button.place(relx=0.55, rely =0.005, relwidth=0.2, relheight = 0.3)
        self.clear_button = Button (self.frame_2, text = 'LIMPAR ESPAÇOS', command = self.cleaning_vendas)
        self.clear_button.place(relx=0.75, rely =0.005, relwidth=0.2, relheight = 0.3)

        self.lista_vendas.bind('<ButtonRelease-1>', self.select_entry_vendas)

    def tela_custos_despesas(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.75)
        self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_2.place(relx=0.01, rely = 0.74, relwidth=0.98, relheight=0.25)

        self.lista_cd = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5'), selectmode = 'extended')
        self.lista_cd.heading("#0", text = "")
        self.lista_cd.heading("#1", text = "ID")
        self.lista_cd.heading("#2", text = "Nome")
        self.lista_cd.heading("#3", text = "Valor")
        self.lista_cd.heading("#4", text = "Data")
        self.lista_cd.heading("#5", text = "Categoria")

        self.lista_cd.column("#0", width =25)
        self.lista_cd.column("#1", width =75)
        self.lista_cd.column("#2", width =175)
        self.lista_cd.column("#3", width =125)
        self.lista_cd.column("#4", width =175)
        self.lista_cd.column("#5", width =175)
        
        self.lista_cd.place(relx=0.0001, rely = 0.07, relwidth = 0.975, relheight=0.7)

        self.cd_label = Label(self.frame_1, text = 'CUSTOS E DESPESAS')
        self.cd_label.place(relx=0.4, rely=0.01, relwidth=0.2, relheight=0.05)

        self.id_label_cd = Label(self.frame_1, text = "ID")
        self.id_label_cd.place(relx = 0.05, rely = 0.8, relwidth = 0.05, relheight = 0.05)
        self.cd_id = Entry(self.frame_1, text = 'ID')
        self.cd_id.place(relx = 0.05, rely = 0.85, relwidth = 0.05, relheight = 0.08)
        self.nome_label_cd = Label(self.frame_1, text = "Nome")
        self.nome_label_cd.place(relx = 0.1, rely = 0.8, relwidth = 0.2, relheight = 0.05)
        self.cd_nome = Entry(self.frame_1, text = 'Nome')
        self.cd_nome.place(relx = 0.1, rely = 0.85, relwidth = 0.2, relheight = 0.08)
        self.valor_label_cd = Label(self.frame_1, text = "Valor")
        self.valor_label_cd.place(relx = 0.3, rely = 0.8, relwidth = 0.15, relheight = 0.05)
        self.cd_valor = Entry(self.frame_1, text = 'Valor')
        self.cd_valor.place(relx = 0.3, rely = 0.85, relwidth = 0.15, relheight = 0.08)
        self.data_label_cd = Label(self.frame_1, text = "Data")
        self.data_label_cd.place(relx = 0.45, rely = 0.8, relwidth = 0.15, relheight = 0.05)
        self.cd_data = Entry(self.frame_1, text = 'DATA')
        self.cd_data.place(relx=0.45, rely = 0.85, relwidth = 0.15, relheight = 0.08)
        self.categoria_label_cd = Label(self.frame_1, text = "Categoria")
        self.categoria_label_cd.place(relx = 0.6, rely = 0.8, relwidth = 0.15, relheight = 0.05)
        self.cd_selected_categoria = StringVar()
        self.cd_categoria = ttk.Combobox(self.frame_1, textvariable = self.cd_selected_categoria, height = 12)
        self.cd_categoria['values'] = ('Custo', 'Despesa')
        self.cd_categoria['state'] = 'readonly'                        
        self.cd_categoria.pack()
        self.categoria_cd = self.cd_selected_categoria.get()
        self.cd_categoria.place(relx = 0.6, rely = 0.85, relwidth = 0.15, relheight = 0.08)

        self.add_cd = Button(self.frame_1, text = 'ADICIONAR', command =lambda: self.submit_cd(self.cd_categoria.current()))
        self.add_cd.place(relx=0.78, rely= 0.8, relwidth=0.2, relheight=0.13)
        self.limpar_cd = Button(self.frame_2, text = 'LIMPAR', command = self.cleaning_cd)
        self.limpar_cd.place(relx= 0.2, rely = 0.005, relwidth=0.2, relheight=0.45)
        self.atualizar_cd = Button(self.frame_2, text = 'UPDATE', command=self.update_cd)
        self.atualizar_cd.place(relx= 0.4, rely = 0.005, relwidth=0.2, relheight=0.45)
        self.deletar_cd = Button(self.frame_2, text = 'DELETAR', command =self.data_remove_cd)
        self.deletar_cd.place(relx= 0.6, rely = 0.005, relwidth=0.2, relheight=0.45)

        self.voltar_tela = Button(self.frame_2, text = "VOLTAR", command=lambda: self.button_callback("tela_inicial"))
        self.voltar_tela.place(relx= 0.01, rely = 0.25, relwidth=0.15, relheight=0.6)
        self.see_each_cd = Button(self.frame_2, text = 'VER C/D', command=lambda: self.button_callback("tela_cd"))
        self.see_each_cd.place(relx= 0.84, rely = 0.25, relwidth=0.15, relheight=0.6)

        self.scroll_lista = Scrollbar(self.frame_1, orient='vertical')
        self.lista_cd.configure(yscroll = self.scroll_lista.set)
        self.scroll_lista.place(relx=0.97, rely =0.07, relwidth=0.03, relheight = 0.7)

        self.lista_cd.bind('<ButtonRelease-1>', self.select_cd)

## TODO continuar depois
    def tela_cd(self):
        self.frame_base = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_base.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.15)
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.16, relwidth=0.98, relheight=0.83)

        self.sel_mes_label = Label(self.frame_base, text = 'Selecione o mês em específico')
        self.sel_mes_label.place(relx=0.175, rely=0.05, relwidth=0.2, relheight=0.3)

        self.sel_mes = StringVar()
        self.sel_mes_box = ttk.Combobox(self.frame_base, textvariable = self.sel_mes, height=13)
        self.sel_mes_box['values'] = ('Mês','1','2','3','4','5','6','7','8','9','10','11','12')
        self.sel_mes_box['state'] = 'readonly'                        
        self.sel_mes_box.set('Mês')
        self.sel_mes_box.place(relx = 0.2, rely = 0.5, relwidth = 0.15, relheight = 0.4)

##TODO implementar funcionalidade dos botões depois
        self.aplicar_mes = Button(self.frame_base, text = 'APLICAR')
        self.aplicar_mes.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.4)     
        self.limpar_mes = Button(self.frame_base, text = 'LIMPAR')
        self.limpar_mes.place(relx=0.602, rely=0.4, relwidth=0.2, relheight=0.4)

        self.label_c = Label(self.frame_1, text = 'Custos')
        self.label_c.place(relx=0.05, rely=0, relwidth=0.4, relheight=0.1)
        self.label_d = Label(self.frame_1, text = 'Despesas')
        self.label_d.place(relx=0.55, rely=0, relwidth=0.4, relheight=0.1)

        self.lista_c = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4'), selectmode = 'extended')
        self.lista_c.heading("#0", text = "")
        self.lista_c.heading("#1", text = "ID")
        self.lista_c.heading("#2", text = "Nome")
        self.lista_c.heading("#3", text = "Valor")
        self.lista_c.heading("#4", text = "Data")

        self.lista_c.column("#0", width =1)
        self.lista_c.column("#1", width =20)
        self.lista_c.column("#2", width =75)
        self.lista_c.column("#3", width =25)
        self.lista_c.column("#4", width =75)

        self.lista_c.place(relx=0.02, rely = 0.105, relwidth = 0.46, relheight=0.6)

        self.lista_d = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4'), selectmode = 'extended')
        self.lista_d.heading("#0", text = "")
        self.lista_d.heading("#1", text = "ID")
        self.lista_d.heading("#2", text = "Nome")
        self.lista_d.heading("#3", text = "Valor")
        self.lista_d.heading("#4", text = "Data")

        self.lista_d.column("#0", width =1)
        self.lista_d.column("#1", width =20)
        self.lista_d.column("#2", width =75)
        self.lista_d.column("#3", width =25)
        self.lista_d.column("#4", width =75)

        self.lista_d.place(relx=0.52, rely = 0.105, relwidth = 0.46, relheight=0.6)

        separator3 = ttk.Separator(root, orient='vertical', style = 'Separator.TSeparator')
        separator3.place(relx=0.5, rely=0.2, relwidth=0, relheight=0.6)

        self.voltar_tela_cd = Button(self.frame_1, text = "VOLTAR GERAL", command=lambda: self.button_callback("tela_custos_despesas"))
        self.voltar_tela_cd.place(relx= 0, rely = 0.85, relwidth=0.2, relheight=0.15)

    def tela_relatorios(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.98)

        style = ttk.Style()
        style.configure("Separator.TSeparator", background="#CCCCCC")

        # separator = ttk.Separator(root, orient='horizontal', style = 'Separator.TSeparator')
        # separator.place(relx=0.5, rely=0.04, relheight=0.865)
        #separator2 = ttk.Separator(root, orient='vertical', style = 'Separator.TSeparator')
        #separator2.place(relx=0.51, rely=0.68, relwidth=0.46)
        separator3 = ttk.Separator(root, orient='vertical', style = 'Separator.TSeparator')
        separator3.place(relx=0.04, rely=0.9, relwidth=0.9)
        
        self.ponto_equilibrio_label = Label(self.frame_1, text = 'Ponto de Equilibrio')
        self.ponto_equilibrio_label.place(relx=0.4, rely=0.02, relwidth=0.2, relheight=0.04)

        #   margem de contribuição = valor das vendas – custos variáveis + despesas variáveis

        #   mc = vendas - custos

        #   (despesa / mc) * 100 = ponto de equilibrio 

        #   (custos fixos + despesas fixas - gastos não desembolsáveis) / margem de contribuição

        self.lista_pe = ttk.Treeview(self.frame_1, height = 3, column=('col1', 'col2', 'col3', 'col4', 'col5'), selectmode = 'extended')
        self.lista_pe.heading('#0', text = '')
        self.lista_pe.heading('#1', text = 'Dia')
        self.lista_pe.heading('#2', text = 'Valor Recebido')
        self.lista_pe.heading('#3', text = 'Valor Gasto')
        self.lista_pe.heading('#4', text = 'Diferença do Dia')
        self.lista_pe.heading('#5', text = 'Diferença Total')

        self.lista_pe.column('#0', width = 1)
        self.lista_pe.column('#1', width = 75)
        self.lista_pe.column('#2', width = 125)
        self.lista_pe.column('#3', width = 125)
        self.lista_pe.column('#4', width = 125)
        self.lista_pe.column('#5', width = 125)
        self.lista_pe.place(relx=0.001, rely=0.25, relwidth=0.98, relheight=0.6)
        
        
        self.mes_pe = StringVar()
        self.sel_mes_pe = ttk.Combobox(self.frame_1, textvariable=self.mes_pe, height = 12 )
        self.sel_mes_pe['values'] = tuple(range(1,13))
        self.sel_mes_pe['state'] = 'readonly'
        self.sel_mes_pe.pack()
        self.sel_mes_pe.place(relx=0.37, rely = 0.1, relwidth=0.05, relheight=0.05)
        self.sel_mes_pe_label = Label(self.frame_1, text = 'Mês')
        self.sel_mes_pe_label.place(relx=0.3, rely=0.1, relwidth=0.05, relheight=0.05)

        
        self.pe_valor = Label(self.frame_1, text=f'Valor diário = {self.pe_valor_mes}')
        self.pe_valor.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)
        #self.pe_valor.config(text=month_text)
        self.pe_saldo = Label(self.frame_1, text=f'Saldo = {self.pe_saldo_mes}')
        self.pe_saldo.place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.05)

        self.lista_pe_check = Button(self.frame_1, text = 'Verificar Mês', command = self.lista_ponto_eq)
        self.lista_pe_check.place(relx=0.45, rely=0.1, relwidth=0.2, relheight=0.05)

        
        #self.retorno_investimento_label = Label(self.frame_1, text = 'Retorno Investimento')
        #self.retorno_investimento_label.place(relx=0.65, rely=0.70, relwidth=0.2, relheight=0.04)
        


        self.voltar_tela = Button(self.frame_1, text = "VOLTAR", command=lambda: self.button_callback("tela_inicial"))
        self.voltar_tela.place(relx= 0, rely = 0.93, relwidth=0.2, relheight=0.07)
        self.tela_diario_b = Button(self.frame_1, text = "DIÁRIO", command=lambda: self.button_callback("tela_diario"))
        self.tela_diario_b.place(relx= 0.5, rely = 0.93, relwidth=0.2, relheight=0.07)
        self.tela_semana_b = Button(self.frame_1, text = "SEMANAL", command=lambda: self.button_callback("tela_semanal"))
        self.tela_semana_b.place(relx= 0.7, rely = 0.93, relwidth=0.2, relheight=0.07)

    def tela_diario(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.98)

        self.mes_diario = StringVar()
        self.sel_mes_diario = ttk.Combobox(self.frame_1, textvariable=self.mes_diario, height = 12 )
        self.sel_mes_diario['values'] = tuple(range(1,13))
        self.sel_mes_diario['state'] = 'readonly'
        self.sel_mes_diario.pack()
        self.sel_mes_diario.place(relx=0.02, rely = 0.2, relwidth=0.05, relheight=0.05)
        self.sel_mes_diario_label = Label(self.frame_1, text = 'Mês')
        self.sel_mes_diario_label.place(relx=0.02, rely=0.15, relwidth=0.05, relheight=0.05)


        self.lista_diaria = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4'), selectmode = 'extended')
        self.lista_diaria.place(relx=0.3, rely=0.2, relwidth=0.7, relheight=0.7)
        self.lista_diaria.heading("#0", text = "")
        self.lista_diaria.heading("#1", text = "Dia")
        self.lista_diaria.heading("#2", text = "Valor Recebido")
        self.lista_diaria.heading("#3", text = "Valor Gasto")
        self.lista_diaria.heading("#4", text = "Diferença Total")

        self.lista_diaria.column("#0", width = 1)
        self.lista_diaria.column("#1", width = 75)
        self.lista_diaria.column("#2", width = 125)
        self.lista_diaria.column("#3", width = 125)
        self.lista_diaria.column("#4", width = 125)

        self.mes_diario = Button(self.frame_1, text = 'VERIFICAR MÊS', command =self.lista_diario_pe)
        self.mes_diario.place(relx= 0.08, rely = 0.2, relwidth=0.2, relheight=0.05)



        self.voltar_tela = Button(self.frame_1, text = "VOLTAR", command=lambda: self.button_callback("tela_relatorios"))
        self.voltar_tela.place(relx= 0, rely = 0.93, relwidth=0.2, relheight=0.07)

    def tela_semanal(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 2)
        self.frame_1.place(relx=0.01, rely = 0.01, relwidth=0.98, relheight=0.98)

        self.mes_semanal = StringVar()
        self.sel_mes_semanal = ttk.Combobox(self.frame_1, textvariable=self.mes_semanal, height = 10 )
        self.sel_mes_semanal['values'] = tuple(range(1,13))
        self.sel_mes_semanal['state'] = 'readonly'
        self.sel_mes_semanal.pack()
        self.sel_mes_semanal.place(relx=0.02, rely = 0.2, relwidth=0.05, relheight=0.05)
        self.sel_mes_semanal_label = Label(self.frame_1, text = 'Mês')
        self.sel_mes_semanal_label.place(relx=0.02, rely=0.15, relwidth=0.05, relheight=0.05)


        self.lista_semanal = ttk.Treeview(self.frame_1, height=3, column=('col1', 'col2', 'col3', 'col4','col5'), selectmode = 'extended')
        self.lista_semanal.place(relx=0.3, rely=0.2, relwidth=0.7, relheight=0.7)
        self.lista_semanal.heading("#0", text = "")
        self.lista_semanal.heading("#1", text = "Dia")
        self.lista_semanal.heading("#2", text = "Até o Dia")
        self.lista_semanal.heading("#3", text = "Valor Recebido")
        self.lista_semanal.heading("#4", text = "Valor Gasto")
        self.lista_semanal.heading("#5", text = "Diferença Total")

        self.lista_semanal.column("#0", width = 1)
        self.lista_semanal.column("#1", width = 75)
        self.lista_semanal.column("#2", width = 75)
        self.lista_semanal.column("#3", width = 125)
        self.lista_semanal.column("#4", width = 125)
        self.lista_semanal.column("#5", width = 125)

        self.mes_semanal = Button(self.frame_1, text = 'VERIFICAR MÊS', command =self.lista_semanal_pe)
        self.mes_semanal.place(relx= 0.08, rely = 0.2, relwidth=0.2, relheight=0.05)



        self.voltar_tela = Button(self.frame_1, text = "VOLTAR", command=lambda: self.button_callback("tela_relatorios"))
        self.voltar_tela.place(relx= 0, rely = 0.93, relwidth=0.2, relheight=0.07)


App()