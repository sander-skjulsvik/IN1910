# Random walks - Tilfeldig tur

## En 1d random walk
    Beveger seg på en tallinje.
    Xn er en stokastisk variabel
    Objeket starter i X0

### random_walk1D_.py

    py: går 100 tilfeldige steg med lengde fra -1 til 1
    vectorized: går N tilfeldige steg, med lengde fra -1 til 1

    skal time det, se forelesning.

## Kan vi si noe om hvordan et gjennomsnitlig object vil bevege seg.
    Vi ser på m forskjellige.

## Gjennomsnitlig forsyvning
    Gjennomsnitt:
        Xn+1 = Xn+Kn
    Gjennomsnitt er en linear operasjon:
        ...
    ...

## Root mean Square - Kvadrarisk gjennomsnitt
    Kvadrert gjennomsnitt:
        $(Xn+1)^2 = (Xn + Kn)^2$
        ...
        ...

    Gjennomsnittlig kvadrert forsyvning øker med N.

## Vaianse
    Var(X) = E((X-E(X))^2) = E(X^2) - E(X^2)

## Myntkast og Law of large Numbers
    I N myntkast hva er forholdet mellom kron og mynt
    Non relative deviation vill increase by sqrt(N)
    LoLN - Når størrelsen på dataene øker vil snittet gå mot forventingsverdien
    Med andre ord:
        #heads/#tails -> 0.5, as N -> infinite