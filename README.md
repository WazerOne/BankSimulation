# BankSimulation
This is my mathematical model of queuing system with 2 tellers.
In this particular model we have 2 parameters of the system: mu represents average of treatments per unit of time and lambda represents average of incoming clients per unit of time.
When we have mu and lambda we can easily calculate ro. Ro represents system's intensity.
(we have constant n=2 tellers)
We have 4 different workload indicators:
1). If ro << n then the system is underloaded - it is beneficial for the client - there are no queues, but unprofitable for the owner - extra cash desks, large downtime
2). If ro < n the system is balanced for the client - acceptable queues, non-critical downtime
3). If ro <= n the system is balanced for the owner - large queues of customers, little to none downtime
4). If ro > n the system is overloaded - beneficial for the owner - there are more applications than possible to handle, but unprofitable for the client - an infinitely growing queue
And 11 different states of system where
state0: 0 customers in system (both tellers are idling, 0 customers in queue)
state1: 1 customer in system (1 teller is busy, 1 teller is idling, 0 customers in queue)
state2: 2 customers in system (both tellers are busy, 0 customers in queue)
state3: 3 customers in system (both tellers are busy, 1 customer in queue)
...
state11: >11 customers in system (both tellers are busy, >9 customers in queue)

In the result(Results.xlsx) of main program(SMO 2 kanala.py) we can see the percentage of time for each state system have been.
In the following program(proverka.py) we can make sure that random generation is following Poisson's destribution.
