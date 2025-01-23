"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):

    return record[1]


def convert_coordinate(coordinate):

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
 
    cordinate_a = azara_record[1]
    cordinate_r = rui_record[1]
    
    return cordinate_r == tuple(cordinate_a)

def create_record(azara_record, rui_record):

    cordinate_a = azara_record[1]
    cordinate_r = rui_record[1]
    if cordinate_r == tuple(cordinate_a):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):

    combined_record = ""
    for item in combined_record_group:
        newrecord=[]
        for num, value in enumerate(item):
            if num != 1:
                if num == 3:
                    newrecord.append(f"{value}")
                else:
                    newrecord.append(f"'{value}'")
            
                    
                
        single_record = f"({', '.join(newrecord)})"
        combined_record += single_record + "\n"
    print(combined_record)
    return combined_record



# to print out the return value.
extract = get_coordinate(('Scrimshawed Whale Tooth', '2A'))
convert = convert_coordinate("2A")
compare = compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
create = create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
cleanUp = clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))

print( 'Extract Coordinate:', extract, 'Format Coordinates:', convert, 'Match Coordinates:', compare, 'Combined Matched Records:', create, 'report of all records:', cleanUp)