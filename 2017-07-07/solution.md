# How Many Critics Does It Take to Find the Best Movie?

This is my solution to the 2017-07-07 [Riddler][1].

## Question

You run a film magazine, _Groovy Movies_, and you have been invited to
attend a new film festival. The festival organizers will screen 30
films evenly distributed across three different screens. Each film
will premiere at this festival, and you want to get the scoop on which
one was the best. The problem is, though, that because there are three
screens, you don’t know which screen will show the best film. You
could watch only Screen A, see the best movie there and report on it,
but it may not be as good as one of the movies on Screen B or C.

Some more details you know from your many years of experience in the
magazine biz:

- Whenever a film is playing on one screen, the other two screens
also have a film playing. But there is enough time between each movie
that one person can always watch the nth round on one screen and the
_n_+1th round on another screen.

- The best movie on one screen will never play at the same time as the
best movie on another screen. However, you don’t know what time slots
they will occupy for each theater.

- All of your reviewers are good rankers — they won’t have any
disagreement about which movies are better than others that they’ve
seen. (They’re ordinal reviewers, in other words.)

- That said, all of your reviewers are terrible raters, so they cannot
give an objective measure of how good a movie was (a 9 out of 10, say)
and compare it to another reviewer’s measure of how good a different
movie was. (To put it another way: They aren’t cardinal reviewers.)

With all that in mind, if you want to know for sure what the best film
at the festival was, what is the minimum number of reviewers you would
need to send to the festival?

_Extra credit_: What if there were more movies shown per screen? What
if there were more screens?

## Solution

First, notice that at least one critic must have seen both the two
best movies, otherwise we will not be able to tell them apart. It
could happen that the best movie is in the first slot and the second
best is in the second slot. Hence, we need three critics watching each
movie in the first slot, then dispersing to watch a different movie at
the second screening. After the first two screenings, we have maximum
three candidates for best movie.

If two movies cannot be told apart, it means that they will have been
shown at the same time and hence we know that at least one of them
will be beaten on the same screen later. We can now keep
redistributing the critics such that those  three who watched a
candidate for best movie go to different screens in the next round. If
we have less than three candidate movies, just distribute the
remaining critics evenly. At no point will we have more than three
candidates. In the end, we will have identified the best movie.

For the Extra credit, notice that we can keep running this scheme no
matter the length of the festival. In general, to cover _N_ screens we
need _N_<sup>2</sup> critics.

## The Question in the Title

The title of the article actually asks a different question. The
answer to the question "How many critics does it take to rank all the
movies?" is that it is not possible in general. To see this, imagine a
festival where the three worst movies were shown on different screens
in the first slot. Since a critic can only watch one of the films,
there would be no way to tell them apart.

[1]: https://fivethirtyeight.com/features/how-many-critics-does-it-take-to-rank-all-the-movies/