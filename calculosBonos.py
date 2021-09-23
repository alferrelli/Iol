# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:55:01 2021

@author: aferrelli
"""
from datetime import date

def calcularInteresCorrido(fdesde,fhasta,tasa,diasanio):
    cantidaddias = days360(fdesde, fhasta)
    ic = tasa * cantidaddias/diasanio
    return ic


def calcularParidad(d1,d2,precio,valorresidual,tasa):
    ic = calcularInteresCorrido(d1, d2, tasa, 360)
    paridad = precio / (valorresidual + ic)
    return paridad*100




def days360(start_date, end_date, method_eu=False):
    # copiada de aca
    # https://stackoverflow.com/questions/51832672/pandas-excel-days360-equivalent
    # reformé el return, porque para mi estaba mal calculado aunque el resultado de bien
    
    # si vienen las fechas desordenadas, las ordeno
    if start_date > end_date:
        temp = start_date
        start_date = end_date
        end_date = temp
    
    
    start_day = start_date.day
    start_month = start_date.month
    start_year = start_date.year
    end_day = end_date.day
    end_month = end_date.month
    end_year = end_date.year
    
    if (
            start_day == 31 or
            (
                method_eu is False and
                start_month == 2 and (
                    start_day == 29 or (
                        start_day == 28 and
                        start_date.is_leap_year is False
                    )
                )
            )
        ):
            start_day = 30
    
    if end_day == 31:
            if method_eu is False and start_day != 30:
                end_day = 1
    
                if end_month == 12:
                    end_year += 1
                    end_month = 1
                else:
                    end_month += 1
            else:
                end_day = 30
                
   # dias desde el año 0 hasta la fecha hasta, le resto
   # dias desde el año 0 hasta la fecha desde
   #me da la diferencia en dias 
    return ( 
              (end_day + ((end_month-1) * 30) + end_year * 360) -
              (start_day + ((start_month-1) * 30) + start_year * 360)
             )
            
    
    # return (
    #         end_day + end_month * 30 + end_year * 360 -
    #         start_day - start_month * 30 - start_year * 360)
            
            