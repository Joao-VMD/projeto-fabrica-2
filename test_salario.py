import streamlit as st

st.set_page_config(page_title="Calculadora de Salário", page_icon="💼")

idioma = st.selectbox("Escolha o idioma / Choose language", ["Português", "English"])

textos = {
    "Português": {
        "titulo": "Calculadora de Salário ",
        "carga": "Digite sua carga horária semanal:",
        "valor_hora": "Digite o valor da sua hora trabalhada:",
        "botao": "Calcular",
        "bruto": "Salário bruto: R$ {:.2f}",
        "inss": "Desconto INSS: R$ {:.2f}",
        "ir": "Desconto IR: R$ {:.2f}",
        "fgts": "Depósito FGTS (8%): R$ {:.2f}",
        "liquido": "Salário líquido: R$ {:.2f}"
    },
    "English": {
        "titulo": "Salary Calculator ",
        "carga": "Enter your weekly working hours:",
        "valor_hora": "Enter your hourly wage:",
        "botao": "Calculate",
        "bruto": "Gross salary: ${:.2f}",
        "inss": "INSS deduction: ${:.2f}",
        "ir": "IR deduction: ${:.2f}",
        "fgts": "FGTS deposit (8%): ${:.2f}",
        "liquido": "Net salary: ${:.2f}"
    }
}

st.title(textos[idioma]["titulo"])

carga_semanal = st.number_input(textos[idioma]["carga"], min_value=0.0, step=1.0)
valor_hora = st.number_input(textos[idioma]["valor_hora"], min_value=0.0, step=0.5)

horas_mes = carga_semanal * 4.5
salario_bruto = valor_hora * horas_mes


# -------- Funções específicas do aplicativo -------- #

def calcular_inss(salario):
    if salario <= 1320:
        return salario * 0.075
    elif salario <= 2571.29:
        return salario * 0.09
    elif salario <= 3856.94:
        return salario * 0.12
    else:
        return salario * 0.14

def calcular_ir(salario):
    if salario <= 2112:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075 - 158.40
    elif salario <= 3751.05:
        return salario * 0.15 - 370.40
    elif salario <= 4664.68:
        return salario * 0.225 - 651.73
    else:
        return salario * 0.275 - 884.96

def calcular_fgts(salario):
    return salario * 0.08  # 8%


# -------- Botão de cálculo -------- #

if st.button(textos[idioma]["botao"]):
    desconto_inss = calcular_inss(salario_bruto)
    desconto_ir = calcular_ir(salario_bruto - desconto_inss)
    fgts = calcular_fgts(salario_bruto)
    salario_liquido = salario_bruto - desconto_inss - desconto_ir

    st.info(textos[idioma]["bruto"].format(salario_bruto))
    st.warning(textos[idioma]["inss"].format(desconto_inss))
    st.warning(textos[idioma]["ir"].format(desconto_ir))
    st.info(textos[idioma]["fgts"].format(fgts))
    st.success(textos[idioma]["liquido"].format(salario_liquido))


# -------- Feedback -------- #

try:
    st.feedback("stars")
except:
    st.write(" Obrigado por usar a calculadora!")
