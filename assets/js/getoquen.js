$.ajax({
    url:'http://34.102.135.155/mapfre/tokenEquifax/',
    type: 'POST',
    success: res => {
        var tokenEquifax = res.token;
        localStorage.setItem('tokenEquifax',tokenEquifax);

    },
    error: e => {
        localStorage.setItem('tokenEquifax',null);
    }
});