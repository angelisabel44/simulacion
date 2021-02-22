f <- function(x) { return(1 / (exp(x) + exp(-x))) }

simulacion_MC <- function(F, a, b, cantidad) {
  acumumulado <- 0
  for (i in 1:cantidad) {
    x <- runif(1)
    acumumulado <- acumumulado + F(a + (b - a) * x)
  }
  return(((b - a) * acumumulado) / cantidad)
}

desde <- 3
hasta <- 7
cantidad <- 50000
replicas <- 30

for (i in 1:replicas) {
  integral <- simulacion_MC(f, desde, hasta, cantidad)
  print(paste("Replica ", i, ": ", integral, sep = ""))
}