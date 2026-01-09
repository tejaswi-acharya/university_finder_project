//fetch = function used for making HTTP requests to fetch resources
//        (eg. json data, images, files)
//        fetch(url,{options}) i.e resource as url and object of options

async function search_uni(){

    const country = document.getElementById("country").value.trim()
    const uniName = document.getElementById("university").value.trim()
    const results = document.getElementById("output") // we will be inserting the contents inside div with id=output using this results variable later

    if (!country){
        window.alert("Please enter a valid country name!")
        return
    }

    let url = `http://127.0.0.1:8000/universities?country=${country}`

    if(uniName){
        url+= `&name=${uniName}`
    }
    results.innerHTML="Fetching....."

    try{
        const response = await fetch(url)
        const data = await response.json()

        results.innerHTML="" //to insert the unniversities found after fetching...leaving it as an empty container

        if (data.length == 0){
            results.innerHTML="No universities found!"
            return
        }
        
        //creating a container/box for each university detail to be stored 

        data.forEach(uni => {
            const box = document.createElement("div")

            box.innerHTML=`
            <h3>${uni.name}</h3>
            <p><strong>Country:</strong> ${uni.country}</p>
                <p>
                    <a href="${uni.web_pages[0]}" target="_blank">
                        Visit Website
                    </a>
                </p>
            `
            results.appendChild(box)
            
        });


    }
    catch(error){
        results.innerHTML("Error fetching data!")
        console.error(error)
    }

}




