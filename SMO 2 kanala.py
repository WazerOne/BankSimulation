#Система массового обслуживания. 2-х канальная с очередью. mu = 9 lam = 12

import numpy as np
import math
import random
import pandas as pd

mu = 9 #Скорость обработки заявок
lam = 12 #Скорость поступления заявок в систему
ro = lam/mu #Нагруженность системы

class Calculate:
    def __init__(self):
        self.clock = 0.0                    #время
        self.state_T1 = 0                   #состояние первого обработчика
        self.state_T2 = 0                   #состояние второго обработчика
        self.t_arrival = self.gen_arrival() #время прибытия
        self.t1_departure = float('inf')    #время отбытия от первого обработчика
        self.t2_departure = float('inf')    #время отбытия от второго обработчика
        self.num_in_q = 0                   #очередь клиентов
        self.num_arrivals = 0               #общее кол-во клиентов
        self.state0_sum = 0                 #бездействие системы
        self.state1_sum = 0                 #один из двух обработчиков работали
        self.state2_sum = 0                 #оба обработчика работали
        self.state3_sum = 0                 #была очередь(1 чел)
        self.state4_sum = 0                 #была очередь(2 чел)
        self.state5_sum = 0                 #была очередь(3 чел)
        self.state6_sum = 0                 #была очередь(4 чел)
        self.state7_sum = 0                 #была очередь(5 чел)
        self.state8_sum = 0                 #была очередь(6 чел)
        self.state9_sum = 0                 #была очередь(7 чел)
        self.state10_sum = 0                #была очередь(8 чел)
        self.state11_sum = 0                #была очередь(9 чел)

    def time_adv(self):
        t_next_event = min(self.t_arrival, self.t1_departure, self.t2_departure)
        if (self.state_T1 == 0) and (self.state_T2 == 0):
            self.state0_sum += t_next_event - self.clock
        if ((self.state_T1 == 1) and (self.state_T2 == 0)) or ((self.state_T1 == 0) and (self.state_T2 == 1)):
            self.state1_sum += t_next_event - self.clock
        if (self.state_T1 == 1) and (self.state_T2 == 1) and (self.num_in_q == 0):
            self.state2_sum += t_next_event - self.clock
        if self.num_in_q == 1:
            self.state3_sum += t_next_event - self.clock
        elif self.num_in_q == 2:
            self.state4_sum += t_next_event - self.clock
        elif self.num_in_q == 3:
            self.state5_sum += t_next_event - self.clock
        elif self.num_in_q == 4:
            self.state6_sum += t_next_event - self.clock
        elif self.num_in_q == 5:
            self.state7_sum += t_next_event - self.clock
        elif self.num_in_q == 6:
            self.state8_sum += t_next_event - self.clock
        elif self.num_in_q == 7:
            self.state9_sum += t_next_event - self.clock
        elif self.num_in_q == 8:
            self.state10_sum += t_next_event - self.clock
        elif self.num_in_q >= 9:
            self.state11_sum += t_next_event - self.clock
        self.clock = t_next_event

        if self.t_arrival < self.t1_departure and self.t_arrival < self.t2_departure:
            self.arrival()
        elif (self.t1_departure == self.t_arrival) and (self.t2_departure == self.t_arrival):
            if np.random.choice([0, 1]) == 1:
                self.state_T1 = 1
                self.dep1 = self.gen_service_time()
                self.t1_departure = self.clock + self.dep1
                self.t_arrival = self.clock + self.gen_arrival()
            else:
                self.state_T2 = 1
                self.dep2 = self.gen_service_time()
                self.t2_departure = self.clock + self.dep2
                self.t_arrival = self.clock + self.gen_arrival()
        elif self.t1_departure == self.t_arrival:
            self.teller1()
            self.arrival()
        elif self.t2_departure == self.t_arrival:
            self.teller2()
            self.arrival()
        elif (self.t1_departure < self.t_arrival) and (self.t1_departure < self.t2_departure):
            self.teller1()
        else:
            self.teller2()

    def arrival(self):
        self.num_arrivals += 1
        if self.num_in_q == 0:
            if (self.state_T1 == 1) and (self.state_T2 == 1):
                self.num_in_q += 1
                self.t_arrival = self.clock + self.gen_arrival()
            elif (self.state_T1 == 0) and (self.state_T2 == 0):
                if np.random.choice([0, 1]) == 1:
                    self.state_T1 = 1
                    self.dep1 = self.gen_service_time()
                    self.t1_departure = self.clock + self.dep1
                    self.t_arrival = self.clock + self.gen_arrival()
                else:
                    self.state_T2 = 1
                    self.dep2 = self.gen_service_time()
                    self.t2_departure = self.clock + self.dep2
                    self.t_arrival = self.clock + self.gen_arrival()
            elif (self.state_T1 == 0) and (self.state_T2 == 1):
                self.dep1 = self.gen_service_time()
                self.t1_departure = s.clock + self.dep1
                self.t_arrival = self.clock + self.gen_arrival()
                self.state_T1 = 1
            else:
                self.dep2 = self.gen_service_time()
                self.t2_departure = self.clock + self.dep2
                self.t_arrival = self.clock + self.gen_arrival()
                self.state_T2 = 1
        else:
            self.num_in_q += 1
            self.t_arrival = self.clock + self.gen_arrival()

    def teller1(self):
        if self.num_in_q > 0:
            self.dep1 = self.gen_service_time()
            self.t1_departure = self.clock + self.dep1
            self.num_in_q -= 1
        else:
            self.t1_departure = float('inf')
            self.state_T1 = 0

    def teller2(self):
        if self.num_in_q > 0:
            self.dep2 = self.gen_service_time()
            self.t2_departure = self.clock + self.dep2
            self.num_in_q -= 1
        else:
            self.t2_departure = float('inf')
            self.state_T2 = 0
    def gen_arrival(self):
        return -np.log(1-np.random.uniform(low=0.0, high=1.0)) / lam
    def gen_service_time(self):
        return -np.log(1-np.random.uniform(low=0.0, high=1.0)) / mu


s = Calculate()
df = pd.DataFrame(columns=['Среднее время между прибытиями',
                           'Кол-во посетителей',
                           'state 0',
                           'state 1',
                           'state 2',
                           'state 3',
                           'state 4',
                           'state 5',
                           'state 6',
                           'state 7',
                           'state 8',
                           'state 9',
                           'state 10',
                           'state 11'])

for i in range(100):
    np.random.seed(i)
    s.__init__()
    while s.clock <= 100:
        s.time_adv()
    a = pd.Series([s.clock / s.num_arrivals,
                   s.num_arrivals,
                   s.state0_sum / s.clock,
                   s.state1_sum / s.clock,
                   s.state2_sum / s.clock,
                   s.state3_sum / s.clock,
                   s.state4_sum / s.clock,
                   s.state5_sum / s.clock,
                   s.state6_sum / s.clock,
                   s.state7_sum / s.clock,
                   s.state8_sum / s.clock,
                   s.state9_sum / s.clock,
                   s.state10_sum / s.clock,
                   s.state11_sum / s.clock],
                  index=df.columns)
    df = df.append(a, ignore_index=True)
df.to_excel('Results.xlsx')



