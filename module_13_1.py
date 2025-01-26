import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')    
    for i in range(6):
        if i == 0:
            continue
        await asyncio.sleep(1/power)   
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    participant_1 = asyncio.create_task(start_strongman('Pasha', 3))
    participant_2 = asyncio.create_task(start_strongman('Denis', 4))
    participant_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await participant_1
    await participant_2
    await participant_3


asyncio.run(start_tournament())
