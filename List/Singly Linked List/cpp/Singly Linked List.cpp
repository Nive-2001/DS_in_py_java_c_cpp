#include <iostream>
using namespace std;

struct Node { 
  int data; 
  Node *next; 
};


class sll {
    Node* head;
    public:
        sll(){
            head=NULL;
        }
        Node* node(int data){
            Node* new_node=new Node;
            new_node->data=data;
            new_node->next=NULL;
        }
        void insert(int data,bool end=false){
            if(end){
                if(this->head==NULL){
                    this->head=node(data);
                }
                else{
                    Node* temp=this->head;
                    while(temp->next){
                        temp=temp->next;
                    }
                    temp->next=node(data);
                }
            }
            else{
                Node* temp=node(data);
                temp->next=this->head;
                this->head=temp;
            }
        }
        void delete(int data,bool end=false,all=false){
            
        }
        void display(){
            Node* temp=this->head;
            while(temp){
                cout<<temp->data<<"- ";
                temp=temp->next;
            }
            cout<<endl;
        }
};

int main() {
	sll head;
    head.insert(5);
    head.insert(6,false);
    head.display();
	return 0;
}
