from datetime import timedelta

from databay import Link
from databay.inlets.random_int_inlet import RandomIntInlet
from databay.outlet import Outlet
from databay.planners import SchedulePlanner
from databay.record import Record

class PrintOutlet(Outlet):

    async def push(self, records:[Record], update):
        for record in records:
            print(update, record.payload)

random_int_inlet = RandomIntInlet()
print_outlet = PrintOutlet()

link = Link(random_int_inlet, print_outlet,
            interval=timedelta(seconds=2), name='print_outlet')

planner = SchedulePlanner()
planner.add_link(link)
planner.start()