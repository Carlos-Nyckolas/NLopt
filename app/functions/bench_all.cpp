// #include <nlopt.hpp>
// #include <iostream>
// #include <iomanip>
// #include <fstream>
// #include <stdio.h>
// #include <stdlib.h>
// #include "benchmarking.h"
// #include "seed.h"
// using namespace std;

// typedef struct {
//     double a, b;
// } my_constraint_data;

// int teste;
// int cont=0;
// int psize=0;
// int problem_type=0;
// double fit;
// ofstream outfile;
// ofstream outfile_fulldata;
// double myvfunc(const std::vector<double> &x, std::vector<double> &grad, void *my_func_data)
// {
// 	++cont;
// 	Benchmarking bench;
// 	fit = bench.execute(problem_type,x);	
// 	if (cont < 3000) {
// 		outfile << cont << " " << fit<< "\n";
// 		outfile_fulldata << cont << " " << fit;
// 		for (int contp=0; contp < psize; contp++)
// 			outfile_fulldata << " " << x[contp]<< "\n";
// 	}
// 	return fit;
// //	else
// //		return -1.0;
// }
// double myvconstraint(const std::vector<double> &x, std::vector<double> &g ad, void *data)
// {
//     my_constraint_data *d = reinterpret_cast<my_constraint_data*>(data);
//     double a = d->a, b = d->b;
//     if (!grad.empty()) {
//         grad[0] = 3 * a * (a*x[0] + b) * (a*x[0] + b);
//         grad[1] = -1.0;
//     }
//     return ((a*x[0] + b) * (a*x[0] + b) * (a*x[0] + b) - x[1]);
// }


// int main(int argc, char ** argv) {
// /*
// 	argv1 - Algorithm type (1-isres, 2-directl, 3-crs2, 4-gmlsl, 5-gs-to-go
// 	argv2 - Problem Type (	1-Ackley, 2-Rastriging, 3-Schwefel, 
// 				4-Lennard-Jones, 5-HyperEllipsoid
// 				6-Rosenbrock, 7-Michalewicz 
// 				8- THz Surface Application)

// 	argv3 - psize is dimensions of the problems
// 	argv4 - number of tests to be performed
// 	argv5 - low value limit 
// 	argv6 - up value limit
// 	argv7 - ouput file basename 

// */
// 	int idalgorithm		= atoi(argv[1]);
// 	problem_type  		= atoi(argv[2]);
// 	psize  				= atoi(argv[3]);
// 	int ptests 			= atoi(argv[4]);
// 	double lowvalue 	= atof(argv[5]);
// 	double upvalue  	= atof(argv[6]);
// 	char basename [100];
// 	sprintf(basename,"%s",argv[7]);
// 	nlopt::opt optx(nlopt::GN_ISRES,psize);
// 	nlopt::opt opt2(nlopt::GN_ISRES, psize);
// 	nlopt::opt opt3(nlopt::GN_DIRECT_L, psize);
// 	nlopt::opt opt4(nlopt::GN_CRS2_LM, psize);
// 	nlopt::opt opt5(nlopt::LN_COBYLA, psize);
// 	nlopt::opt opt6(nlopt::LN_BOBYQA, psize);
// 	nlopt::opt opt7(nlopt::LN_NEWUOA_BOUND, psize);
// 	nlopt::opt opt8(nlopt::LN_SBPLX, psize);
// 	nlopt::opt opt9(nlopt::LD_MMA, psize);
// 	nlopt::opt opt10(nlopt::LD_CCSAQ, psize);
// 	nlopt::opt opt11(nlopt::LD_SLSQP, psize);
// 	nlopt::opt opt12(nlopt::LD_LBFGS, psize);
// 	nlopt::opt opt13(nlopt::LD_TNEWTON_PRECOND_RESTART, psize);
// 	nlopt::opt opt14(nlopt::LD_TNEWTON_PRECOND, psize);
// 	nlopt::opt opt15(nlopt::LD_TNEWTON, psize);
// 	nlopt::opt opt16(nlopt::LD_VAR1, psize);
// 	nlopt::opt opt_temp(nlopt::LD_MMA, psize);
// 	std::vector<double> lb(2);
// 	std::vector<double> ub(2);
// 	std::vector<double> x(2);
// 	double minf;
// 	Seed seed;
// 	double limits[7];
//     limits[0] = 3;
//     limits[1] = lowvalue;
//     limits[2] = upvalue;
//     limits[3] = 0;
//     limits[4] = 1;
//     limits[5] = 10;
//     limits[6] = 1;
// 	char filename[100];
// 	char filenamefull[100];
// 	for (teste=0; teste < ptests; teste++) {
// 		// Defining outfile name to store into the Results benchmark analysis
// 		// optimization type
// 		switch (idalgorithm) {
// 			case 2:
// 				optx = opt2;
// 				sprintf(filename,"%s/isres_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/isres_test_%d_full.dat", basename, teste);
// 			break;
// 			case 3:
// 				optx = opt3;
// 				sprintf(filename,"%s/direct-l_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/direct-l_test_%d_full.dat", basename, teste);
// 			break;
// 			case 4:
// 				optx = opt4;
// 				sprintf(filename,"%s/crs2_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/crs2_test_%d_full.dat", basename, teste);
// 			break;
// 			/*case 4:
// 				optx = opt4;
// 				sprintf(filename,"%s/gd_sto-go_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/gd_sto-go_test_%d_full.dat", basename, teste);
// 			break;*/
// 			case 5:
// 				optx = opt5;
// 				sprintf(filename,"%s/ln_cobyla_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ln_cobyla_test_%d_full.dat", basename, teste);
// 			break;
// 			case 6:
// 				optx = opt6;
// 				sprintf(filename,"%s/ln_bobyqa_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ln_bobyqa_test_%d_full.dat", basename, teste);
// 			break;
// 			case 7:
// 				optx = opt7;
// 				sprintf(filename,"%s/ln_newuoa_bound_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ln_newuoa_bound_test_%d_full.dat", basename, teste);
// 			break;
// 			case 8:
// 				optx = opt8;
// 				sprintf(filename,"%s/ln_sbplx_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ln_sbplx_test_%d_full.dat", basename, teste);
// 			break;
// 			case 9:
// 				optx = opt9;
// 				sprintf(filename,"%s/ld_mma_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_mma_test_%d_full.dat", basename, teste);
// 			break;
// 			case 10:
// 				optx = opt10;
// 				sprintf(filename,"%s/ld_ccsaq_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_ccsaq_test_%d_full.dat", basename, teste);
// 			break;
// 			case 11:
// 				optx = opt11;
// 				sprintf(filename,"%s/ld_slsqp_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_slsqp_test_%d_full.dat", basename, teste);
// 			break;
// 			case 12:
// 				optx = opt12;
// 				sprintf(filename,"%s/ld_lbfgs_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_lbfgs_test_%d_full.dat", basename, teste);
// 			break;
// 			case 13:
// 				optx = opt13;
// 				sprintf(filename,"%s/ld_tnewton_precond_restart_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_tnewton_precond_restart_test_%d_full.dat", basename, teste);
// 			break;
// 			case 14:
// 				optx = opt14;
// 				sprintf(filename,"%s/ld_tnewton_precond_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_tnewton_precond_test_%d_full.dat", basename, teste);
// 			break;
// 			case 15:
// 				optx = opt15;
// 				sprintf(filename,"%s/ld_tnewton_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_tnewton_test_%d_full.dat", basename, teste);
// 			break;
// 			case 16:
// 				optx = opt16;
// 				sprintf(filename,"%s/ld_var1_test_%d.dat", basename, teste);
// 				sprintf(filenamefull,"%s/ld_var1_test_%d_full.dat", basename, teste);
// 			break;
// 		}
// 		cout << "Filename::: " << filename << "   filenamefull:: " << filenamefull << "\n";
// 		outfile.open(filename);
// 		outfile_fulldata.open(filenamefull);
// 		lb.resize(psize);
// 		ub.resize(psize);
// 		x.resize(psize);
// 		cout << "psize:::::: " << psize << "\n";
// 		for (int i=0; i < psize; i++) {
// 			limits[1] = lb[i] = lowvalue;
// 			limits[2] = ub[i] = upvalue;
// 			x[i]  = seed.randOption(limits);
// 		}
// 		optx.set_lower_bounds(lb);
// 		optx.set_upper_bounds(ub);
// 		optx.set_min_objective(myvfunc, NULL);
// 		optx.set_xtol_rel(1e-4);
// 		optx.set_maxeval(3000);
// 		nlopt::result result = optx.optimize(x, minf);
// 		for (int i=cont; i < 3000; i++) {
// 			outfile << i << " " << fit<< "\n";
// 			outfile_fulldata << i << " " << fit;
// 		}
// 		outfile.close();
// 		outfile_fulldata.close();
// 		cont = 0;
// 	}
// 	return 0;
// }
