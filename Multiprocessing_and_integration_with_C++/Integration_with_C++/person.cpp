#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
                int fib();  //addition of new method
	private:
		int age;
                int fib_rec(int); // private recursion 
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}


//addition of the new function in the method
//fib_rec follows the same process as in python 
int Person::fib_rec(int n) {   
  if (n<=1) {
    return n;
  } else {
    return fib_rec(n-1)+fib_rec(n-2);
  }
}

int Person::fib() {
  return fib_rec(age);
}


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
        int Person_fib(Person* person) {return person->fib();}
        void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
	}
       }

