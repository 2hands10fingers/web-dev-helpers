import csv
the_file = 'collegetest2.csv'

with open(the_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        school = line[0].rstrip()
        program = line[1].rstrip()
        city = line[2].rstrip()
        first_name = line[3].rstrip()
        last_name = line[4].rstrip()
        email = line[5].rstrip()
        x = f"""
          <div class="row">
            <div class="first-item-col col-sm-3">{school}</div>
            <div class="second-item-col col-sm-3">{program}</div>
            <div class="third-item-col col-sm-3">{city}</div>
            <div class="fourth-item-col col-sm-3">
	            <span>{first_name} {last_name}</span><br>
	            <span class="college-email">{email.lower()}</span>
            </div>
          </div>
		"""
        print(x)
