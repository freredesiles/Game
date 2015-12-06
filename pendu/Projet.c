#include <stdio.h>
#include "graphsimple.h"
#define hauteur 600
#define longueur 800
#include "hasard.h"
#include <math.h>
#define g 9.81


 void FairePoint(int x[100], int y[100],int a, int niveau,int x1rec,int y1tab[100],int x2rec,int y2tab[100])
{
   int i;
   for(i=0;i<a;i++)
   {

      CerclePlein(x[i],y[i],3);
      if(niveau == 4 && i == 0)
         {
            
            SuppRectangle(x1rec,y1tab[i],x2rec,y2tab[i]);
               
         }
      
      if(niveau == 4)
         {
            Rectangle(x1rec,y1tab[i],x2rec,y2tab[i]);
	    AttendreDelai(100.0);
            SuppRectangle(x1rec,y1tab[i],x2rec,y2tab[i]);
         }
      else if(niveau < 4)
	 {
	    AttendreDelai(100.0);
	 }
      
         
   }
      
 }       
      
      
void Fenetre(int x1, int y1, int x2, int y2, int x1mur, int x2mur, int y2mur)
   {
       
      
      Initialiser(longueur,hauteur);   /* Affiche la fenetre */
      Ligne(0,550,longueur,550);       /* Affiche le sol */
      Triangle(30,520,50,525,43,542);  /* Affiche un triangle pour l'arc */
      Ligne(30,537,60,518);            /* Affiche la fleche */
      Rectangle(x1,y1,x2,y2);          /* créer la cible */
      RectanglePlein(x1mur,550,x2mur,y2mur); /*Affiche un mur*/                               

   }


float Trajectoire(float x, float vitesse, float angle)
   {
      float y,yo=52.8;
     
      y=((g*(x*x))/(2*vitesse*vitesse*cos(angle)*cos(angle)))-(tan(angle)*(x))+yo;   
      
      return y;
   }
   
   
int ErreurDistance(int valeurX, int valeurY)
   {
            
     if(valeurY > 570)
        {
                    
            return 2;
        }
     if(valeurX > 780)
       {
                    
            return 1;
                     
       }
    else
       {
           return 0;
       }
  }
  
  
 int CaTouche( int valeurX[100], int valeurY[100],int x1rec,int x2rec,int y1tab[100],int y2tab[100],int x1mur,int x2mur,int y1mur,int y2mur, int i)        
       {   
               if(valeurX[i] > x1rec && valeurX[i] < x2rec && valeurY[i] > y1tab[i] && valeurY[i] < y2tab[i])
                  {
                       
                     return 2;                                              /* Arrete le processus si un point est dans le rectangle */
                     
                  }
               else if(valeurX[i] > x1mur && valeurX[i] < x2mur && valeurY[i] < y1mur && valeurY[i] > y2mur)
                  {
                     
                     return 1;
                  }
                else
                {
                  return 0;
                }
         }
     
         
void valeur(float *vitesse, float *angle)
   {
        printf("Inserer une valeur de vitesse");
        scanf("%f",vitesse);
        do
        {
        printf("Inserer un angle");
        scanf("%f",angle);
        }while(*angle == 90);
   }
     
       
       
int TracerTrajectoire(int *nbjouer,float angle, float vitesse, int x1rec, int y1rec, int x2rec, int y2rec, int x1mur, int y1mur, int x2mur, int y2mur, int *niveau)        
   {
      int x,i=0,valeurX[100],valeurY[100],test1, test2, y1tab[100], y2tab[100],changer;
      
      y1tab[0] = y1rec;
      y2tab[0] = y2rec;
      
      for(x=0;x<80;x++)                                             /* 80 car longueur de notre fenetre graphique est de 80 */
         {  
              valeurX[i] = (x*10)+37;                                         /* Transforme nos valeurs en pixels */
              valeurY[i] = (Trajectoire(x,vitesse,angle))*10;
              
              test1 = ErreurDistance(valeurX[i], valeurY[i]);
               
              if(test1 == 2)
                {    
                    break;
                }
                
               if(*niveau == 4)
                  {
		     if(i==0)
			{
			     changer = 400 - y1rec;
			     
			     if(changer > 0)
				{
				    changer = 0;
				}
			     else
				{
				    changer = 1;
				}
			}
			
                     if(changer == 1 && i > 0)
                     	{
                             y1tab[i] = y1tab[i-1] - 10;
                             y2tab[i] = y2tab[i-1] - 10;
			     
			     if(y1tab[i] < 310)
				{
				     changer = 0;
				}
                     	}
                     else if(changer == 0 && i > 0)
                     	{  
                             y1tab[i] = y1tab[i-1] +10;
                             y2tab[i] = y2tab[i-1] +10;
			     

			     if(y2tab[i] > 540)
				{
				     changer = 1;
				}
                     	}
                  
                  }
		  else
		     {
			y1tab[i] = y1rec;
			y2tab[i] = y2rec;
		     }

              test2 = CaTouche(valeurX, valeurY, x1rec, x2rec, y1tab, y2tab, x1mur, x2mur, y1mur, y2mur, i);
               
              if(test2 == 1 || test2 == 2)
                 { 
                    
                     
                     if(test2 == 2)
                        {
                           FairePoint(valeurX,valeurY,i,*niveau,x1rec,y1tab,x2rec,y2tab);
                           printf(" ca touche !\n");
                           return 1;
                        }
                     FairePoint(valeurX,valeurY,i,*niveau,x1rec,y1tab,x2rec,y2tab);
                     printf(" t'as touche le mur !\n");
                     return 0;
                     
                 }
                 
               
               i++;     
          }
                     
               
      FairePoint(valeurX,valeurY,i,*niveau,x1rec,y1tab,x2rec,y2tab);
      
      if(test1 == 2)
         {
            printf(" ça touche le sol ! ");
         }
      else if(test1 == 1)
         {
            printf(" Trop loin !");
         }
      nbjouer++; 
      return 0; 
   }
        
                 
int main()
   {
      float vitesse,angle,ratio,score=0.0;
      int x1rec,x2rec,y1rec,y2rec,nbjouer=0,x1mur,x2mur,y2mur,mode,niveau = 1;
      char rejouer;
      do
         {
         
            printf("Bienvenue ! A quelle mode voulez vous jouer ? \n");
            printf(" 1-Mode libre, \n 2-Mode challenge");
            scanf("%d",&mode);
            
            if(mode==1)
               {

                  
            
                  x1rec = hasard(600,750);
                  y1rec = hasard(300,500);
                  x2rec = x1rec + 20;
                  y2rec = y1rec + 50;
                  x1mur = hasard(200,400);
                  x2mur = x1mur + 40;
                  y2mur = hasard(250,400);
                  
   
   
                  Fenetre(x1rec,y1rec,x2rec,y2rec,x1mur,x2mur,y2mur);
                  
                  valeur(&vitesse, &angle);
   
                  angle = (angle * 3.14)/180.0;                            /* transforme degré en radian */

                  TracerTrajectoire(&nbjouer,angle,vitesse,x1rec,y1rec,x2rec,y2rec,x1mur,550,x2mur,y2mur,&niveau);
                  Clore();
                  
                 
               }
               
             else if(mode==2)
                {
                     int nbvie = 30, b=0,test = 0;
                     
                     printf(" 1er niveau vous avez %d vie \n",nbvie);
                  
                     while(test != 1 && nbvie != 0)            /* Niveau 1 */
                        {
                     
                           if(b==0)                      /* Permet de ne pas reinitialiser la fenetre à chaque fois */
                              {
                                 x1rec = hasard(600,750);
                                 y1rec = hasard(300,500);
                                 x2rec = x1rec + 20;
                                 y2rec = y1rec + 50;
                              }
                           b++;
                           Fenetre(x1rec,y1rec,x2rec,y2rec,550,550,550);
                           valeur(&vitesse, &angle);
                           angle = (angle * 3.14)/180.0; 
                           test = TracerTrajectoire(&nbjouer,angle,vitesse,x1rec,y1rec,x2rec,y2rec,550,550,550,550,&niveau);
                           printf("%d",test);
                           if(test !=1)
                              {
                                 nbvie--;
                              }
                           Clore();
                           printf(" Il vous reste %d vie !\n",nbvie);
                        }
                        niveau++;
                        test=0;
                       
                      while(test != 1 && nbvie != 0)           /* Niveau 2 */
                        {
                           printf(" 2eme niveau vous avez %d vie \n",nbvie);
                           
                                 x1rec = hasard(600,750);         /* Dans le niveau 2 la cible change de place à chaque tire raté */      
                                 y1rec = hasard(300,500);
                                 x2rec = x1rec + 20;
                                 y2rec = y1rec + 50;
                             
                           
                           Fenetre(x1rec,y1rec,x2rec,y2rec,550,550,550);
                           valeur(&vitesse, &angle);
                           angle = (angle * 3.14)/180.0; 
                           test = TracerTrajectoire(&nbjouer,angle,vitesse,x1rec,y1rec,x2rec,y2rec,550,550,550,550,&niveau);
                           if(test !=1)
                              {
                                 nbvie--;
                              }
                           Clore();
                        }
                        niveau++;
                        test=0;
                        b=0;
                        while(test != 1 && nbvie != 0)            /* Niveau 3 */
                        {
                     
                           if(b==0)                      /* Apparition d'un mur qui ne change pas de place après un coup manqué */
                              {
                                 x1rec = hasard(600,750);
                                 y1rec = hasard(300,500);
                                 x2rec = x1rec + 20;
                                 y2rec = y1rec + 50;
                                 x1mur = hasard(200,400);
                                 x2mur = x1mur + 40;
                                 y2mur = hasard(250,400);
                              }
                           b++;
                           Fenetre(x1rec,y1rec,x2rec,y2rec,x1mur,x2mur,y2mur);
                           valeur(&vitesse, &angle);
                           angle = (angle * 3.14)/180.0; 
                           test = TracerTrajectoire(&nbjouer,angle,vitesse,x1rec,y1rec,x2rec,y2rec,x1mur,550,x2mur,y2mur,&niveau);
                           if(test !=1)
                              {
                                 nbvie--;
                              }
                           Clore();
                           printf(" Il vous reste %d vie !\n",nbvie);
                        }
                        niveau++;
                        test=0;
                        
                        b=0;
                        
                        while(test != 1 && nbvie != 0)            /* Niveau 4 */
                        {
                     
                           if(b==0)                      /* cible bouge en temps réel */
                              {  
                                 x1rec = hasard(600,750);
                                 y1rec = hasard(300,500);
                                 x2rec = x1rec + 20;
                                 y2rec = y1rec + 50;
                                 x1mur = hasard(200,400);
                                 x2mur = x1mur + 40;
                                 y2mur = hasard(250,400);
                              }
                           b++;
                           
                           Fenetre(x1rec,y1rec,x2rec,y2rec,x1mur,x2mur,y2mur);
                           valeur(&vitesse, &angle);
                           
                           angle = (angle * 3.14)/180.0; 
                           test = TracerTrajectoire(&nbjouer,angle,vitesse,x1rec,y1rec,x2rec,y2rec,x1mur,550,x2mur,y2mur,&niveau);
                           if(test !=1)
                              {
                                 nbvie--;
                              }
                           Clore();
                           printf(" Il vous reste %d vie !\n",nbvie);
                        }
                         niveau++;                        
                                             
                 }                             
         
                  do
                     {  
                        printf("Voulez-vous rejouer?");
                        scanf(" %c",&rejouer);
                        if( rejouer == 'n')
                           {
                              ratio = (score/nbjouer)*100;
                              printf("Votre score est de %.1f, pourcentage de réussite %f %% \n",score,ratio);
                           }
               
                     }while( rejouer != 'o' && rejouer != 'n');
      
               
               
     
       }while(rejouer =='o');
 
   return 0;
}
