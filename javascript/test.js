var movies = [
    { name: 'pushpa', isWatched: true, isHit: true },
    { name: 'leo', isWatched: false, isHit: true },
    { name: 'bheemla nayak', isWatched: true, isHit: false }
];

movies.forEach(movie => {
    var watchStatus = movie.isWatched ? "I watched" : "I have not seen";
    var hitStatus = movie.isHit ? "Hit!!!" : "Flop!!!!";

    console.log(`# ${watchStatus} ${movie.name} and movie is ${hitStatus}`);
});
