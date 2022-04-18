# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 04:38:21 2022

@author: jahop_fz60h0
"""

import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests

from PIL import Image

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_hxwcQt.json")




st_lottie(lottie_hello, key = "hello")

st.title("Para que conozcas a quienes votaron en contra de la Reforma Eléctrica del, Lic. AMLO")
st.header("Página web, creada por: Javier Horacio Pérez Ricárdez")

st.subheader("")

#1 as sidebar menu

#with st.sidebar:
#      selected = option_menu(
#          menu_title = "Main Menu", #requerid
#          options = ["Home", "Projects", "Contact"], #required
#          icons = ["house","book", "envelope"], #optional
#          menu_icon = "cast", #optional
#          default_index = 0,
#      )

#1 vertical menu
selected = option_menu(
    menu_title = "Por partido político", #required
    options = ["PAN", "PRI", "MC", "PRD", "MORENA"], #required
    icons = ["", "", "",""], #optional
    menu_icon = "cast", #optional
    default_index = 0, #optional
    
    ) 

 

#2 horizontal menu
#selected = option_menu(
#    menu_title = "Menú principal ------------------------------------------->  jahoperi", #required
#    options = ["Inicio", "Proyecto1", "Proyecto2", "CV", "Contacto"], #required
#    icons = ["house", "book", "envelope"], #optional
#    menu_icon = "cast", #optional
#    default_index = 0, #optional
#    orientation = "horizontal",
#)    



                    
if selected == "PAN":
   st.title(f"Has seleccionado {selected}")
   st.header("Diputados del Partido Acción Nacional que votaron en contra: 113")
   st.subheader("")
   st.subheader("1: Aguado Romero Paulina")
   st.subheader("")
   image = Image.open('1.jpg')
   st.image(image)
   st.subheader("2: Aguilar Coronado Marco Humberto")
   st.subheader("")
   image = Image.open('2.jpg')
   st.image(image)
   st.subheader("3: Almaraz Smer Oscar de Jesús")
   st.subheader("")
   image = Image.open('3.jpg')
   st.image(image)
   st.subheader("4: Almendariz Puppo Marco Antonio")
   st.subheader("")
   image = Image.open('4.jpg')
   st.image(image)
   st.subheader("5: Álvarez Hernández Daniela Soraya")
   st.subheader("")
   image = Image.open('5.jpg')
   st.image(image)
   st.subheader("6: Aranda Orozco Ana Teresa")
   st.subheader("")
   image = Image.open('6.jpg')
   st.image(image)
   st.subheader("7: Azar Figueroa Anuar Roberto")
   st.subheader("")
   image = Image.open('7.jpg')
   st.image(image)
   st.subheader("8: Azuara Zúñiga Xavier")
   st.subheader("")
   image = Image.open('8.jpg')
   st.image(image)
   st.subheader("9: Báez Guerrero José Luis")
   st.subheader("")
   image = Image.open('9.jpg')
   st.image(image)
   st.subheader("10: Balderas Hernández Itzel Josefina")
   st.subheader("")
   image = Image.open('10.jpg')
   st.image(image)
   
   st.subheader("11: Balderas Trejo Ana María")
   st.subheader("")
   image = Image.open('11.jpg')
   st.image(image)
   st.subheader("12: Beauregard Martínez Carolina")
   st.subheader("")
   image = Image.open('12.jpg')
   st.image(image)
   st.subheader("13: Becerra Moreno Monica")
   st.subheader("")
   image = Image.open('13.jpg')
   st.image(image)
   st.subheader("14: Bolio Pinelo Kathia María")
   st.subheader("")
   image = Image.open('14.jpg')
   st.image(image)
   st.subheader("15: Campuzano González Gina Gerardina")
   st.subheader("")
   image = Image.open('15.jpg')
   st.image(image)
   st.subheader("16: Castell de Oro Palacios María Teresa")
   st.subheader("")
   image = Image.open('16.jpg')
   st.image(image)
   st.subheader("17: Castillo Olivares Héctor Israel")
   st.subheader("")
   image = Image.open('17.jpg')
   st.image(image)
   st.subheader("18: Castrellón Garza Francisco Javier")
   st.subheader("")
   image = Image.open('18.jpg')
   st.image(image)
   st.subheader("19: Chalé Cauich Sergio Enrrique")
   st.subheader("")
   image = Image.open('19.jpg')
   st.image(image)
   st.subheader("20: Cifuentes Negrete Román")
   st.subheader("")
   image = Image.open('20.jpg')
   st.image(image)
   
   
   st.subheader("21: Compeán Fernández Eliseo")
   st.subheader("")
   image = Image.open('21.jpg')
   st.image(image)
   st.subheader("22: Contreras Duarte Laura Patricia")
   st.subheader("")
   image = Image.open('22.jpg')
   st.image(image)
   st.subheader("23: CORDERO GONZALEZ WENDY M.")
   st.subheader("")
   image = Image.open('23.jpg')
   st.image(image)
   st.subheader("24: Creel Miranda Santiago")
   st.subheader("")
   image = Image.open('24.jpg')
   st.image(image)
   st.subheader("25: Díaz Villalón Erika de los Ángeles")
   st.subheader("")
   image = Image.open('25.jpg')
   st.image(image)
   st.subheader("26: Escudero Fabre María del Carmen")
   st.subheader("")
   image = Image.open('26.jpg')
   st.image(image)
   st.subheader("27: Espadas Galván Jorge Arturo")
   st.subheader("")
   image = Image.open('27.jpg')
   st.image(image)
   st.subheader("28: Esquivel Arrona Ana María")
   st.subheader("")
   image = Image.open('28.jpg')
   st.image(image)
   st.subheader("29: Felipe Torres Joanna Alejandra")
   st.subheader("")
   image = Image.open('29.jpg')
   st.image(image)
   st.subheader("30: Galarza Castro Yesenia")
   st.subheader("")
   image = Image.open('30.jpg')
   st.image(image)
   
   
   st.subheader("31: Gamboa Torales María Josefina")
   st.subheader("")
   image = Image.open('31.jpg')
   st.image(image)
   st.subheader("32: García García José Antonio")
   st.subheader("")
   image = Image.open('32.jpg')
   st.image(image)
   st.subheader("33: Garcia Velasco Anabey")
   st.subheader("")
   image = Image.open('33.jpg')
   st.image(image)
   st.subheader("34: Garza Treviño Pedro")
   st.subheader("")
   image = Image.open('34.jpg')
   st.image(image)
   st.subheader("35: Godínez del Rio Enrique")
   st.subheader("")
   image = Image.open('35.jpg')
   st.image(image)
   st.subheader("36: Gómez Cárdenas Annia Sarahí")
   st.subheader("")
   image = Image.open('36.jpg')
   st.image(image)
   st.subheader("37: Gómez del Campo Gurza Mariana")
   st.subheader("")
   image = Image.open('37.jpg')
   st.image(image)
   st.subheader("38: González Alonso Carmen Rocío")
   st.subheader("")
   image = Image.open('38.jpg')
   st.image(image)
   st.subheader("39: González Azcárraga Rosa María")
   st.subheader("")
   image = Image.open('39.jpg')
   st.image(image)
   st.subheader("40: González Márquez Karen Michel")
   st.subheader("")
   image = Image.open('40.jpg')
   st.image(image)
   
  
   st.subheader("41: González Urrutia Wendy")
   st.subheader("")
   image = Image.open('41.jpg')
   st.image(image)
   st.subheader("42: González Zepeda Javier")
   st.subheader("")
   image = Image.open('42.jpg')
   st.image(image)
   st.subheader("43: Gutiérrez Valdez María de los Angeles")
   st.subheader("")
   image = Image.open('43.jpg')
   st.image(image)
   st.subheader("44: Gutierrez Valtierra Diana Estefania")
   st.subheader("")
   image = Image.open('44.jpg')
   st.image(image)
   st.subheader("45: Hernández Escobar Alma Rosa")
   st.subheader("")
   image = Image.open('45.jpg')
   st.image(image)
   st.subheader("46: Huerta Ling Guillermo Octavio")
   st.subheader("")
   image = Image.open('46.jpg')
   st.image(image)
   st.subheader("47: Huerta Villegas Genoveva")
   st.subheader("")
   image = Image.open('47.jpg')
   st.image(image)
   st.subheader("48: Inzunza Armas Jorge Ernesto")
   st.subheader("")
   image = Image.open('48.jpg')
   st.image(image)
   st.subheader("49: Jiménez Angulo Julia Licet")
   st.subheader("")
   image = Image.open('49.jpg')
   st.image(image)
   st.subheader("50: Juárez Navarrete Berenice")
   st.subheader("")
   image = Image.open('50.jpg')
   st.image(image)
   
   
   
   st.subheader("51: Lara Carreón Diana María Teresa")
   st.subheader("")
   image = Image.open('51.jpg')
   st.image(image)
   st.subheader("52: Lixa Abimerhi José Elías")
   st.subheader("")
   image = Image.open('52.jpg')
   st.image(image)
   st.subheader("53: Lopez Sosa Mariela")
   st.subheader("")
   image = Image.open('53.jpg')
   st.image(image)
   st.subheader("54: Loyola Vera Ignacio")
   st.subheader("")
   image = Image.open('54.jpg')
   st.image(image)
   st.subheader("55: Luna Ayala Noemi Berenice")
   st.subheader("")
   image = Image.open('55.jpg')
   st.image(image)
   st.subheader("56: Macías Olvera Felipe Fernando")
   st.subheader("")
   image = Image.open('56.jpg')
   st.image(image)
   st.subheader("57: Macías Zambrano Gustavo")
   st.subheader("")
   image = Image.open('57.jpg')
   st.image(image)
   st.subheader("58: Madrazo Limón Carlos")
   st.subheader("")
   image = Image.open('58.jpg')
   st.image(image)
   st.subheader("59: Mandujano Tinajero Esther")
   st.subheader("")
   image = Image.open('59.jpg')
   st.image(image)
   st.subheader("60: Martínez López Paulo Gonzalo")
   st.subheader("")
   image = Image.open('60.jpg')
   st.image(image)
   
   
   st.subheader("61: Mata Atilano Noel")
   st.subheader("")
   image = Image.open('61.jpg')
   st.image(image)
   st.subheader("62: Mata Carrasco Mario")
   st.subheader("")
   image = Image.open('62.jpg')
   st.image(image)
   st.subheader("63: Mata Lozano Lizbeth")
   st.subheader("")
   image = Image.open('63.jpg')
   st.image(image)
   st.subheader("64: Maturino Manzanera Juan Carlos")
   st.subheader("")
   image = Image.open('64.jpg')
   st.image(image)
   st.subheader("65: Mendoza Acevedo Luis Alberto")
   st.subheader("")
   image = Image.open('65.jpg')
   st.image(image)
   st.subheader("66: Monraz Ibarra Miguel Angel")
   st.subheader("")
   image = Image.open('66.jpg')
   st.image(image)
   st.subheader("67: Montes Estrada Berenice")
   st.subheader("")
   image = Image.open('67.jpg')
   st.image(image)
   st.subheader("68: Morales Flores Jesús Fernando")
   st.subheader("")
   image = Image.open('68.jpg')
   st.image(image)
   st.subheader("69: Murillo Manríquez Sonia")
   st.subheader("")
   image = Image.open('69.jpg')
   st.image(image)
   st.subheader("70: Núñez Cerón Sarai")
   st.subheader("")
   image = Image.open('70.jpg')
   st.image(image)
   

   st.subheader("71: Olvera Coronel Lilia Caritina")
   st.subheader("")
   image = Image.open('71.jpg')
   st.image(image)
   st.subheader("72: Olvera Higuera Claudia Gabriela")
   st.subheader("")
   image = Image.open('72.jpg')
   st.image(image)
   st.subheader("73: Oranday Aguirre Nora Elva")
   st.subheader("")
   image = Image.open('73.jpg')
   st.image(image)
   st.subheader("74: Pacheco Marrufo Rommel Aghmed")
   st.subheader("")
   image = Image.open('74.jpg')
   st.image(image)
   st.subheader("75: Patrón Laviada Cecilia Anunciación")
   st.subheader("")
   image = Image.open('75.jpg')
   st.image(image)
   st.subheader("76: Pérez Díaz Victor Manuel")
   st.subheader("")
   image = Image.open('76.jpg')
   st.image(image)
   
   st.subheader("77: PEREZ JAEN ZERMEÑO MA ELENA")
   st.subheader("NO APARECE")
   #image = Image.open('77.jpg')
   #st.image(image)
   
   st.subheader("78: Quadri de la Torre Gabriel Ricardo")
   st.subheader("")
   image = Image.open('78.jpg')
   st.image(image)
   st.subheader("79: Quintana Martínez Carlos Humberto")
   st.subheader("")
   image = Image.open('79.jpg')
   st.image(image)
   st.subheader("80: Ramírez Barba Éctor Jaime")
   st.subheader("")
   image = Image.open('80.jpg')
   st.image(image)

   
   st.subheader("81: RENDON GARCIA CESAR A.")
   st.subheader("")
   image = Image.open('81.jpg')
   st.image(image)
   st.subheader("82: Reza Gallegos Rocío Esmeralda")
   st.subheader("")
   image = Image.open('82.jpg')
   st.image(image)
   st.subheader("83: Riestra Piña Mario Gerardo")
   st.subheader("")
   image = Image.open('83.jpg')
   st.image(image)
   st.subheader("84: Rivera Gutiérrez Riult")
   st.subheader("")
   image = Image.open('84.jpg')
   st.image(image)
   st.subheader("85: Rocha Acosta Sonia")
   st.subheader("")
   image = Image.open('85.jpg')
   st.image(image)
   st.subheader("86: Rodríguez Rivera Iván Arturo")
   st.subheader("")
   image = Image.open('86.jpg')
   st.image(image)
   st.subheader("87: Romero Herrera Jorge")
   st.subheader("")
   image = Image.open('87.jpg')
   st.image(image)
   st.subheader("88: Romero Hicks Juan Carlos")
   st.subheader("")
   image = Image.open('88.jpg')
   st.image(image)
   st.subheader("89: Romero Velázquez Krishna Karina")
   st.subheader("")
   image = Image.open('89.jpg')
   st.image(image)
   st.subheader("90: Romo Cuéllar Martha Estela")
   st.subheader("")
   image = Image.open('90.jpg')
   st.image(image) 
   
   
   st.subheader("91: Rubio Fernández Paulina")
   st.subheader("")
   image = Image.open('91.jpg')
   st.image(image)
   st.subheader("92: Salgado Almaguer Pedro")
   st.subheader("")
   image = Image.open('92.jpg')
   st.image(image)
   st.subheader("93: Sánchez Velázquez Ana Laura")
   st.subheader("")
   image = Image.open('93.jpg')
   st.image(image)
   st.subheader("94: Sánchez Zepeda Rodrigo")
   st.subheader("")
   image = Image.open('94.jpg')
   st.image(image)
   st.subheader("95: Solórzano Gallego Marcia")
   st.subheader("")
   image = Image.open('95.jpg')
   st.image(image)
   st.subheader("96: Tejeda Cid Armando")
   st.subheader("")
   image = Image.open('96.jpg')
   st.image(image)
   st.subheader("97: Téllez Hernández Héctor Saúl")
   st.subheader("")
   image = Image.open('97.jpg')
   st.image(image)
   st.subheader("98: Terrazas Baca Patricia")
   st.subheader("")
   image = Image.open('98.jpg')
   st.image(image)
   st.subheader("99: Tinajero Robles Desiderio")
   st.subheader("")
   image = Image.open('99.jpg')
   st.image(image)
   st.subheader("100: Torreblanca Engell Santiago")
   st.subheader("")
   image = Image.open('100.jpg')
   st.image(image) 
   
   
   st.subheader("101: TORRES AJURIA HERMINIO")
   st.subheader("")
   image = Image.open('101.jpg')
   st.image(image)
   st.subheader("102: Torres Graciano Fernando")
   st.subheader("")
   image = Image.open('102.jpg')
   st.image(image)
   st.subheader("103: Tovar Vargas José Salvador")
   st.subheader("")
   image = Image.open('103.jpg')
   st.image(image)
   st.subheader("104: Triana Tena Jorge")
   st.subheader("")
   image = Image.open('104.jpg')
   st.image(image)
   st.subheader("105: Valenzuela González Carlos Alberto")
   st.subheader("")
   image = Image.open('105.jpg')
   st.image(image)
   st.subheader("106: Valenzuela Sánchez Ana Laura")
   st.subheader("")
   image = Image.open('106.jpg')
   st.image(image)
   st.subheader("107: Varela Pinedo Miguel Ángel")
   st.subheader("")
   image = Image.open('107.jpg')
   st.image(image)
   st.subheader("108: Verástegui Ostos Vicente Javier")
   st.subheader("")
   image = Image.open('108.jpg')
   st.image(image)
   st.subheader("109: VILLARREAL ELIZONDO YOLANDA")
   st.subheader("")
   image = Image.open('109.jpg')
   st.image(image)
   st.subheader("110: Villarreal García Ricardo")
   st.subheader("")
   image = Image.open('110.jpg')
   st.image(image) 
   
   
   st.subheader("111: Zapata Meraz José Antonio")
   st.subheader("")
   image = Image.open('111.jpg')
   st.image(image)
   st.subheader("112: Zavala Gómez del Campo Margarita Ester")
   st.subheader("")
   image = Image.open('112.jpg')
   st.image(image)
   st.subheader("113: Zepeda Martínez Leticia")
   st.subheader("")
   image = Image.open('113.jpg')
   st.image(image) 
   
   
   
   
   
   
   
   
if selected == "PRI":
   st.title(f"Has seleccionado {selected}") 
   st.subheader("En construcción")
   #st.subheader("")
   #st.subheader("03/04/2022")
   #st.subheader("")
   #st.subheader("https://www.youtube.com/watch?v=1o9LDCbL8_U")
   

if selected == "MC":
      st.title(f"Has seleccionado {selected}") 
      st.subheader("En construcción")
      #st.subheader("11/04/2022")
      #st.subheader("Revocación de mandato")
      #image = Image.open('imagen1.jpg')
      #st.image(image, caption='Ayer fui a votar, por ya sabes quien')  
      

if selected == "PRD":
      st.title(f"Has seleccionado {selected}") 
      st.subheader("En construcción")
      #st.subheader("11/04/2022")
      #image = Image.open('imagen2.jpg')
      #st.image(image, caption='Historia del almacenamiento de datos')       


      
if selected == "MORENA":
   st.title(f"Has seleccionado {selected}") 
   st.subheader("En construcción")
   #st.subheader("jahoperi@gmail.com")


                

