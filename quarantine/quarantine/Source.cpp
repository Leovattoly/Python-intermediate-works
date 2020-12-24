#include <iostream>

using namespace std;

// Base class
class Quarantine_Center {
public:
	int center_id;
	char location[10];
	int quantity_of_beds;
	int no_of_patients;
	long contact_number;

	// Constructor

	Quarantine_Center()
	{
		quantity_of_beds = 20;
	}

};

class Person {
public:
	int person_id;
	char first_name[10];
	char last_name[10];
	char gender;
	int age;
	char blood_group[3];

	// Constructor
};

class Doctor
{
public:
	char name[20];
	int age;
	char specialty[100];
};
// Derived class
class Patient : public Person, Doctor {
public:
	int bed_no;

	// Constructor

	Patient(int b_n)
	{
		if (b_n >= 20) {
			throw "Center is Full!";
		}
		else
			bed_no = b_n;
	}
};

class Corona_Test : public Patient {
public:
	char date[8];
	char time[10];
	int count;
	char result[100];
	// Constructor
};

int main(void) {
	return 0;
}