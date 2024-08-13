echo "anneal.dl8..."; bin/blossom data/anneal.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/anneal_$1.txt; echo "anneal.dl8 done!";
echo "breast-cancer-un.dl8..."; bin/blossom data/breast-cancer-un.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/breast-cancer-un_$1.txt; echo "breast-cancer-un.dl8 done!";
echo "car-un.dl8..."; bin/blossom data/car-un.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/car-un_$1.txt; echo "car-un.dl8 done!";
echo "diabetes.dl8..."; bin/blossom data/diabetes.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/diabetes_$1.txt; echo "diabetes.dl8 done!";
echo "forest-fires-un.dl8..."; bin/blossom data/forest-fires-un.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/forest-fires-un_$1.txt; echo "forest-fires-un.dl8 done!";
echo "hypothyroid.dl8..."; bin/blossom data/hypothyroid.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/hypothyroid_$1.txt; echo "hypothyroid.dl8 done!";
echo "ionosphere.dl8..."; bin/blossom data/ionosphere.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/ionosphere_$1.txt; echo "ionosphere.dl8 done!";
echo "lymph.dl8..."; bin/blossom data/lymph.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/lymph_$1.txt; echo "lymph.dl8 done!";
echo "messidor-bin.dl8..."; bin/blossom data/messidor-bin.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/messidor-bin_$1.txt; echo "messidor-bin.dl8 done!";
echo "pendigits.dl8..."; bin/blossom data/pendigits.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/pendigits_$1.txt; echo "pendigits.dl8 done!";
echo "titanic-un.dl8..."; bin/blossom data/titanic-un.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/titanic-un_$1.txt; echo "titanic-un.dl8 done!";
echo "yeast.dl8..."; bin/blossom data/yeast.dl8 --max_depth 7 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/yeast_$1.txt; echo "yeast.dl8 done!";
echo "expanded_anneal.dl8..."; bin/blossom expanded/expanded_anneal.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_anneal_$1.txt; echo "expanded_anneal.dl8 done!";
echo "expanded_breast-cancer-un.dl8..."; bin/blossom expanded/expanded_breast-cancer-un.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_breast-cancer-un_$1.txt; echo "expanded_breast-cancer-un.dl8 done!";
echo "expanded_car-un.dl8..."; bin/blossom expanded/expanded_car-un.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_car-un_$1.txt; echo "expanded_car-un.dl8 done!";
echo "expanded_diabetes.dl8..."; bin/blossom expanded/expanded_diabetes.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_diabetes_$1.txt; echo "expanded_diabetes.dl8 done!";
echo "expanded_forest-fires-un.dl8..."; bin/blossom expanded/expanded_forest-fires-un.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_forest-fires-un_$1.txt; echo "expanded_forest-fires-un.dl8 done!";
echo "expanded_hypothyroid.dl8..."; bin/blossom expanded/expanded_hypothyroid.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_hypothyroid_$1.txt; echo "expanded_hypothyroid.dl8 done!";
echo "expanded_ionosphere.dl8..."; bin/blossom expanded/expanded_ionosphere.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_ionosphere_$1.txt; echo "expanded_ionosphere.dl8 done!";
echo "expanded_lymph.dl8..."; bin/blossom expanded/expanded_lymph.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_lymph_$1.txt; echo "expanded_lymph.dl8 done!";
echo "expanded_messidor-bin.dl8..."; bin/blossom expanded/expanded_messidor-bin.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_messidor-bin_$1.txt; echo "expanded_messidor-bin.dl8 done!";
echo "expanded_pendigits.dl8..."; bin/blossom expanded/expanded_pendigits.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_pendigits_$1.txt; echo "expanded_pendigits.dl8 done!";
echo "expanded_titanic-un.dl8..."; bin/blossom expanded/expanded_titanic-un.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_titanic-un_$1.txt; echo "expanded_titanic-un.dl8 done!";
echo "expanded_yeast.dl8..."; bin/blossom expanded/expanded_yeast.dl8 --max_depth 5 --test_sample .2 --seed $1 --time 900 --print_sol >> traces/expanded_yeast_$1.txt; echo "expanded_yeast.dl8 done!";