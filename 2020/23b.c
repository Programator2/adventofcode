#include <stdio.h>

struct node {
  int n;
  struct node *next;
  struct node *prev;
};

struct node c[1000001];

struct node *remove_three(struct node *start_node) {
  struct node *left = start_node->prev;
  struct node *last = start_node->next->next;
  struct node *right = last->next;

  left->next = right;
  start_node->prev = NULL;

  right->prev = left;
  last->next = NULL;
  return start_node;
}

void insert_three(struct node *start_node, struct node *where) {
  struct node *left = where;
  struct node *right = where->next;

  left->next = start_node;
  start_node->prev = left;

  struct node *last = start_node->next->next;
  last->next = right;
  right->prev = last;
}

void insert_before(struct node *node, struct node *where) {
  struct node *left = where->prev;

  left->next = node;
  node->prev = left;

  node->next = where;
  where->prev = node;
}

int main() {
  int input[] = {3, 6, 8, 1, 9, 5, 7, 4, 2};
  for (int i=1; i < 1000001; i++)
    c[i].n = i;
  for (int i=10; i < 1000001; i++) {
    c[i].next = c + i + 1;
    c[i].prev = c + i - 1;
  }
  c[10].prev = c + 1000000;
  c[1000000].next = c + 10;
  for (int i = 0; i < 9; i++) {
    insert_before(&c[input[i]], c + 10);
  }

  struct node *current_cup = &c[3];
  for (int i = 0; i < 10000000; i++) {
    int destination = current_cup->n - 1;
    if (destination < 1)
      destination = 1000000;
    struct node *three = remove_three(current_cup->next);
    while (destination == three->n ||
	   destination == three->next->n ||
	   destination == three->next->next->n ||
	   destination == current_cup->n) {
      destination--;
      if (destination < 1)
	destination = 1000000;
    }
    insert_three(three, c + destination);
    current_cup = current_cup->next;
  }

  printf("%lld\n", ((long long) c[1].next->n)*c[1].next->next->n);
}
