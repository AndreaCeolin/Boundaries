library(ggplot2)
library("gridExtra")

GCD_IE = read.table("ie-corr.txt")
GCD_Alt = read.table("alt-corr.txt")
GCD_Uralalt = read.table("ural-alt-corr.txt")

cor.test(GCD_IE$V3, GCD_IE$V4, method = c("pearson"))
cor.test(GCD_IE$V3, GCD_IE$V4, method = c("kendall"))

cor.test(GCD_Alt$V3, GCD_Alt$V4, method = c("pearson"))
cor.test(GCD_Alt$V3, GCD_Alt$V4, method = c("kendall"))

cor.test(GCD_Uralalt$V3, GCD_Uralalt$V4, method = c("pearson"))
cor.test(GCD_Uralalt$V3, GCD_Uralalt$V4, method = c("kendall"))


IE <- ggplot(GCD_IE, aes(x=V3, y=V4)) + 
  geom_point()+
  geom_smooth(method=lm)+
  ggtitle("Indo-European") +
  xlab("Geo") + ylab("Syn")+ theme(plot.title = element_text(hjust=0.5))+
  ylim(0, 0.5)


Alt <- ggplot(GCD_Alt, aes(x=V3, y=V4)) +
  geom_point()+
  geom_smooth(method=lm)+
  ggtitle("Altaic") +
  xlab("Geo") + ylab("Syn")+ theme(plot.title = element_text(hjust=0.5))+
  ylim(0, 0.5)

Uralalt <- ggplot(GCD_Uralic, aes(x=V3, y=V4)) +
  geom_point()+
  geom_smooth(method=lm)+
  ggtitle("Uralo-Altaic") +
  xlab("Geo") + ylab("Syn")+ theme(plot.title = element_text(hjust=0.5))+
  ylim(0, 0.5)

par(mfrow=c(1,3))
grid.arrange(IE, Alt, Uralalt, ncol=3)

