RATES={'Economy':10,'Premium':18,'SUV':25}
SURGE_MULTIPLIER=1.5
PEAK_START=17
PEAK_END=20

def calculate_fare(km,vehicle_type,hour):
    if vehicle_type not in RATES: raise ValueError('Service Not Available')
    base_fare=km*RATES[vehicle_type]
    surge_multiplier=SURGE_MULTIPLIER if PEAK_START<=hour<=PEAK_END else 1.0
    return base_fare*surge_multiplier

def main():
    print('='*42); print('           CITYCAB - FARECALC'); print('='*42)
    try:
        km=float(input('Enter distance (km): ')); hour=int(input('Enter hour of day (0-23): ')); vehicle_type=input('Enter vehicle type (Economy/Premium/SUV): ').strip().title()
        if km<=0: print('Distance must be greater than 0.'); return
        if not 0<=hour<=23: print('Hour must be between 0 and 23.'); return
        fare=calculate_fare(km,vehicle_type,hour); rate=RATES[vehicle_type]; is_peak=PEAK_START<=hour<=PEAK_END; surge_multiplier=SURGE_MULTIPLIER if is_peak else 1.0; base_fare=km*rate
        print('\n'+'='*42); print('              PRICE RECEIPT'); print('='*42); print(f'Vehicle Type     : {vehicle_type}'); print(f'Distance         : {km:.2f} km'); print(f'Rate             : ₹{rate:.2f} / km'); print(f'Base Fare        : ₹{base_fare:.2f}'); print(f'Hour             : {hour:02d}:00'); print(f'Surge Multiplier : {surge_multiplier:.1f}x'); print(f'Final Fare       : ₹{fare:.2f}'); print('='*42); print('Peak-hour surge applied.' if is_peak else 'No surge pricing applied.')
    except ValueError as error:
        if str(error)=='Service Not Available': print('\nService Not Available for that vehicle type.\nAvailable vehicles: Economy, Premium, SUV')
        else: print('\nInvalid input. Please enter valid numbers.')
if __name__=='__main__': main()
