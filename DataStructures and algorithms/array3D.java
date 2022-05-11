public class array3D
{
    public static void main(String[] args) {
        int myArray[][][] = new int[3][4][5];
        for(int i = 0 ; i < 3 ; i++)
        for(int j = 0 ; j < 4 ; j++)
        for(int k = 0 ; k < 5 ; k++)
        myArray[i][j][k] = i*j*k;

        for(int i = 0 ; i < 3 ; i++)
        {
        for(int j = 0 ; j < 4 ; j++)
        {
        for(int k = 0 ; k < 5 ; k++)
        System.out.print(myArray[i][j][k] + " ");
        System.out.println();
        }
        System.out.println();
        }
    }
}