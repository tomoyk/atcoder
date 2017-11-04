#include <math.h>
#include <stdlib.h>
#include <stdio.h>
 
int main(void){
 
  int N;
  int R[1000];
  int S = 0;
 
  // 入力
  scanf("%d",&N);
 
  for(int i=0;i<N;i++) {
    scanf("%d",&R[i]);
    //printf("%d\n", R[i]);
  }
 
  int tmp;
 
  // ソートを実行
  for(int i=0;i<N-1;i++){
    for(int j=N-1;i<j;j--){
      if(R[j-1] > R[j]){
        tmp = R[j];
        R[j] = R[j-1];
        R[j-1] = tmp;
      }
    }
  }
 
  /* デバッグ
  for(int i=0;i<N;i++) {
    printf("%d\n", R[i]);
  } */
 
  //for(int i=0+2;i<N;i+=2){
  for(int i=N-1;i>=0;i--){
    S += pow((double)R[i], 2.0) * ( (N-i)%2==0 ? -1 : 1);
    //printf("%d\n", R[i]);
  }
 
  // 結果の出力
  printf("%.12f\n",(double)S * M_PI);
}
