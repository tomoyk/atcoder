#include <stdio.h>
#include <string.h>
 
int main(){
 
  char memo[27];
  char S[27];
  scanf("%s", S);
  strcpy(memo, S);
 
 
  for(int i=0;i<strlen(S);i++){
    for(int j=i+1;j<strlen(memo);j++){
//      printf("%d-%d\n", i, j);
      if(S[i] == memo[j] && i!=j ){
        printf("no\n");
        return 0;
      }
    }
  }
 
  printf("yes\n");
  return 0;
 
}
