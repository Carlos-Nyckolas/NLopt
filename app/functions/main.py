import nlopt_optimization
import nlopt

opt = nlopt_optimization.NLoptOptimization()

opt.setAlgorithmType(nlopt.LD_MMA)
opt.setLB([-float('inf'), 0])
opt.setXTol(1e-4)
opt.setX([1.234, 5.678])
opt.setNTests(100)
opt.inequality(opt.getX())
opt.executeOptimization()