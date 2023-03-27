#include<iostream>

using namespace std;

struct node{
	int info;
	node *next;
};
struct LinkedList{
	node *head;
 	node *tail;
};

node* createNode(int x){
	node *p;
	p = new  node;
	if(p==NULL){
		cout<<"Khong du bo nho!";
		exit(1);
	}
	p->info = x;
	p->next = NULL;
	return p;
}

void createsList(LinkedList &l){
	l.head = NULL;
	l.tail = NULL;
}

void insertHead(LinkedList &l, int x){
	node *p;
	p = createNode(x);
	if(p==NULL){
		cout<<"Khong tao duoc node!";
		exit(1);
	}
	if(l.head==NULL){//trường hợp danh sách rỗng
		l.head = l.tail = p;
	}else{//trường hợp danh sách không rỗng
		p->next = l.head;
		l.head = p;
	}
}

void processList(LinkedList &l){
	node *p;
	p = l.head;
	while (p!= NULL){
		cout<<p->info<<" ";//xuất giá trị trong node
		p = p->next;
	}
}

node* searchList(LinkedList l, int k){	
	node *p;
	p = l.head;
	while((p!= NULL)&&(p->info != k)){
		p = p->next;
	}
	return p;
}

void deleteList(LinkedList &l){
	node *p;
	while (l.head!= NULL){
		p = l.head;
		l.head = p->next;
		delete p;
	}
	l.tail = NULL;
}

void insertTail(LinkedList &l, int x){
	node *p = createNode(x);
	if(p==NULL){
		cout<<"Khong tao duoc nut moi!";
		exit(1);
	}
	if (l.head==NULL){//trường hợp danh sách rỗng
		l.head =  l.tail = p ;
	}else{//trường hợp danh sách không rỗng
		l.tail->next = p;
		l.tail = p;
	}
}


int main () {
    LinkedList l;
    int n,x;
    cin >> n;
    node *p;
    for (int i = 0;i < n ; i++) {
        cin >> x;
        insertTail(l,x);
    }
    processList(l);
    return 0;
}