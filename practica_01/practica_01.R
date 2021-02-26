f <- function(x) { return(1 / (exp(x) + exp(-x))) }

simulacion_MC <- function(F, a, b, cantidad) {
  acumumulado <- 0
  for (i in 1:cantidad) {
    x <- runif(1)
    acumumulado <- acumumulado + F(a + (b - a) * x)
  }
  return(((b - a) * acumumulado) / cantidad)
}

comparar_digitos <- function(valor) {
  cantidad <- 0
  for (i in 1:6) {
    montecarlo <- signif(valor, digits = i)
    wolfram <- signif(0.048834, digits = i)
    if (montecarlo != wolfram) {
      return(cantidad)
    }
    cantidad <- cantidad + 1
  }
  return(cantidad)
}

desde <- 3
hasta <- 7
replicas <- 30

df_datos <- data.frame("replica" = integer(), "muestra" = integer(), "integral" = numeric(), "digitos" = integer())

muestras <- 10^(4:6)
for (cantidad in muestras) {
  valores <- numeric()
  digitos <- integer()
  for (i in 1:replicas) {
    integral <- simulacion_MC(f, desde, hasta, cantidad)
    numero <- comparar_digitos(integral)
    valores <- c(valores, integral)
    digitos <- c(digitos, numero)
    #print(paste("Replica ", i, ": ", integral, sep = ""))
  }
  df_datos <- rbind(df_datos, data.frame("replica" = 1:replicas, "muestra" = cantidad,
                                         "integral" = valores, "digitos" = digitos))
}

moda <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

df_resultados <- data.frame("muestra" = muestras)
df_resultados$min <- aggregate(df_datos$digitos, by = list(df_datos$muestra), FUN = min)[,2]
df_resultados$media <- aggregate(df_datos$digitos, by = list(df_datos$muestra), FUN = mean)[,2]
df_resultados$mediana <- aggregate(df_datos$digitos, by = list(df_datos$muestra), FUN = median)[,2]
df_resultados$moda <- aggregate(df_datos$digitos, by = list(df_datos$muestra), FUN = moda)[,2]

barplot(df_resultados$moda, names.arg = df_resultados$muestra)

library(ggplot2)
ggplot(data = df_datos, aes(x = as.factor(muestra), y = digitos)) + geom_boxplot()
ggplot(data = df_datos, aes(x = as.factor(muestra), y = digitos)) + geom_violin()
