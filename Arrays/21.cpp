/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/*You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
iterative solution*/ 


#include<iostream>
using namespace std;

class ListNode{
    public:
        int val;
        ListNode *next;
        ListNode(int value){
            val=value;
            next=NULL;
        }
};


void insertAtTail(ListNode *&head, int val){
    ListNode *n = new ListNode(val);
    ListNode *temp = head;
    if(head==NULL){
        head=n;
        return;
    }
    while(temp->next!=NULL){
        temp=temp->next;
    }
    temp->next=n;
}
void display(ListNode *head){
    ListNode *temp = head;
    while(temp!=NULL){
        cout<<temp->val<<endl;
        temp=temp->next;
    }
}
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==NULL){
            return list2;
        }
        if(list2==NULL){
            return list1;
        }
        ListNode *ptr=list1;
        if(list1->val>list2->val){
            ptr=list2;
            list2=list2->next;
        }
        else{
            ptr=list1;
            list1=list1->next;
        }
        ListNode *curr=ptr;
        while(list1 && list2){
            if(list1->val<list2->val){
                curr->next=list1;
                list1=list1->next;
            }
            else{
                curr->next=list2;
                list2=list2->next;
            }
            curr=curr->next;
        }
        if(!list1){
            curr->next=list2;
        }
        else{
            curr->next=list1;
        }
        return ptr;

    }//func ends
};
int main(){
    ListNode *list1 = NULL;
    insertAtTail(list1, 1);
    insertAtTail(list1, 2);
    insertAtTail(list1, 4);
    display(list1);
    ListNode *list2 = NULL;
    insertAtTail(list2, 1);
    insertAtTail(list2, 3);
    insertAtTail(list2, 4);
    display(list2);
    Solution abc;
    ListNode *list3 = NULL;
    cout<<"Solution";
    list3=abc.mergeTwoLists(list1, list2);
    display(list3);
}