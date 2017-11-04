#include <stdio.h>
 
#define DEBUG 0
 
int main(void){
 
  int N,counter,B[20];
 
  // 社員番号i番の給料
  int Money[21];
 
  // 直属の部下を列挙
  int members[40];
 
  // Nの入力
  scanf("%d", &N);
 
  // 社員番号の最大値
  int maximum = 0;
 
  // 社員の上司入力(0は無視して考える)
  for(int i=1;i<N;i++){
    scanf("%d", &B[i]);
 
    if(maximum < B[i])
      maximum = B[i];
  }
 
  // Money配列(直下の社員の給料の和)の初期化
  for(int i=0;i<sizeof(Money)/sizeof(Money[0]);i++){
    Money[i] = 1;
  }
 
  // 社員番号i番の社員の直属部下B[j]を探索
  for(int i=maximum;i>0;i--){
 
    // 社員の部下を列挙
    if(DEBUG) printf("\n--- %d ---\n", i);
 
    // 直属の部下の給料一覧配列の初期化
    for(int j=0;j<sizeof(members)/sizeof(members[0]);j++) members[j]=0;
 
    // 直下の社員の人数
    counter=0;
 
    // 直属の部下を探索
    for(int j=0;j<N;j++){
 
      // 直属の部下のとき
      if(i==B[j]){
 
        // 部下の社員番号の出力
        if(DEBUG) printf("%d, ", j+1);
 
        // 直属の社員一覧配列に社員番号を代入
        members[counter] = Money[j+1];
        counter++;
      }
 
    }
 
    // 部下がいるか
    if(counter == 1) { //部下が1人いる
      if(DEBUG) printf("\nbuka: 1, Money[%d], members[0]=%d\n", i, members[0]);
      Money[i] = 2 * members[0] + 1;
    }else if(counter == 2){ // 部下が2人いる
      if(DEBUG) printf("\nbuka: 2, Money[%d], members[0]=%d, members[1]=%d\n", i, members[0], members[1]);
      Money[i] = members[0] + members[1] + 1;
    }else{ // 部下が3人いる
      if(DEBUG) printf("\nbuka: 3, Money[%d], ", i);
 
      // 最大と最小を求める
      int max=members[0], min=members[0];
      for(int k=0;k<counter;k++){
 
        if(DEBUG) printf("members[%d]=%d\n", k, members[k]);
 
        if( members[k] >= max )
          max = members[k];
 
        if( members[k] <= min )
          min = members[k];
 
      }
 
      if(DEBUG) printf("max: %d, min: %d\n", max, min);
      Money[i] = max + min + 1;
    }
 
    if(DEBUG) printf("Money[%d]=%d\n", i, Money[i]);
    else if(i==1) printf("%d\n", Money[i]);
 
  }
 
}
