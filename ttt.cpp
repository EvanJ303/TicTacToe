#include <iostream>
using namespace std;

void fullprint(int paramBoard[3][3]){
    for (int i=0; i < 3;i++){
        cout<<"\n";
        for (int k=0;k<3;k++){
            cout << paramBoard[i][k] << " ";
        }
    }
}

int main(){
int board[3][3]={{0,0,0},{0,0,0},{0,0,0}};
int x;
int y;
int p=0;
int o=0;

fullprint(board);

while(o==0){
if(p==0){
    cout << "P1 TURN ";
}
else{
    cout << "P2 TURN ";
}

cout << "SELECT ROW";
    cin >> x;
cout << "SELECT COLUMN";
    cin >> y;

if(p==0){
    board[x][y]=1;
    p++;
}
else{
    board[x][y]=2;
    p--;
}

fullprint(board);

}

return 0;
}