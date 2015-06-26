#include <iostream>

using std::cout;
using std::endl;

class A {
  int x,x1;
  int y;

  public:
    virtual void foo();
};

class B : public A {
  int z;

  public:
    virtual void foo();
};

void A::foo() {
  cout << "[A] foo" << endl;
}

void B::foo() {
  cout << "[B] foo" << endl;
}

int main() {
  A* a = new A();
  a->foo();

  B* b = new B();
  b->foo();
}
