def register_party(parties):
    for party in parties:
        party_name = party.get("party_name")
        reg_number = party.get("reg_number")
        member_count = party.get("member_count")
        
        # Checking if member count meets requirements
        if member_count >= 1000:
            print(f"Party '{party_name}' with registration number '{reg_number}' has met the minimum member requirement and can be registered.")
        else:
            print(f"Party '{party_name}' with registration number '{reg_number}' does not have enough members to be registered.")

last_reg_number = 10003318

new_reg_number = last_reg_number + 1

# Information for the new party
mk_party = {"party_name": "MK Party", "reg_number": str(new_reg_number), "member_count": 5300}

register_party([mk_party])

def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
    if voter_id in voter_info:
        if not voter_info[voter_id]["has_voted"]:
            voter_info[voter_id]["name"] = name
            voter_info[voter_id]["voting_district"] = voting_district
            voter_info[voter_id]["has_voted"] = has_voted
            print(f"Voter with ID {voter_id} information updated successfully.")
        else:
            print(f"Voter with ID {voter_id} has already voted.")
    else:
        voter_info[voter_id] = {"name": name, "voting_district": voting_district, "has_voted": has_voted}
        print(f"New voter with ID {voter_id} added successfully.")

voter_info = {
    "V123": {"name": "Nqobani Zuma", "voting_district": "District D", "has_voted": False},
    "V456": {"name": "Thobani Mjadu", "voting_district": "District L", "has_voted": True}
}

update_voter_info(voter_info, "V789", "Rizzoli Jane", "District F", False)  # Adding new voter
update_voter_info(voter_info, "V123", "Maura Alse.", "District N", True)   # Updating existing voter

#SEE

parties_on_ballot = ["ANC", "DA", "EFF", "IFP", "ACDP", "COPE", "FF+", "GOOD", "NFP", "PAC", "UDM", "VF+", "ALJAMA", "ATM", "BLF", "CCTP", "COSATU", "EFFS", "GASP", "GRN", "IFPin", "KOP", "NAMP", "PA", "PBH", "SINDP", "SMME", "VRYHEID", "ZPO"]

party_member_counts = {
    "ANC": 1500000,
    "DA": 800000,
    "EFF": 500000,
    "IFP": 100000,
    "ACDP": 50000,
    "COPE": 30000,
    "FF+": 25000,
    "GOOD": 20000,
    "NFP": 15000,
    "PAC": 10000,
    "UDM": 9000,
    "VF+": 8000,
    "ALJAMA": 7000,
    "ATM": 6000,
    "BLF": 5000,
    "CCTP": 4000,
    "COSATU": 3000,
    "EFFS": 2000,
    "GASP": 1000,
    "GRN": 500,
    "IFPin": 400,
    "KOP": 300,
    "NAMP": 200,
    "PA": 100,
    "PBH": 50,
    "SINDP": 20,
    "SMME": 10,
    "VRYHEID": 5,
    "ZPO": 1
}

parties_with_1000_members = [party for party in parties_on_ballot if party_member_counts.get(party, 0) >= 1000]

print(parties_with_1000_members)

parties_with_1000_members = []

for party in parties_on_ballot:
    member_count = party_member_counts.get(party, 0)
    if member_count >= 1000:
        parties_with_1000_members.append(party)

print(parties_with_1000_members)

voter_records = [
    {"voter_id": 1, "name": "John", "registered": True},
    {"voter_id": 2, "name": "Jane", "registered": False},
    {"voter_id": 3, "name": "Alice", "registered": True},
    {"voter_id": 4, "name": "Bob", "registered": True},
    {"voter_id": 5, "name": "Charlie", "registered": False}
]

registered_voters = list(filter(lambda record: record.get('registered', False), voter_records))

print(registered_voters)