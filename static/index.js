// using the fetch function to get the data necessary
let edu_data;

// storing the data fetched by the fetch api and awaiting the api to return the data transfered
edu_data = await fetch("/api/message")
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => console.error(error));

// Processing the data to then by used by D3js to make bar graphs!!1
let province_list = {
    province_name: "",
    province_subjects: [],
    province_subject_number: []
};
province_list.province_name = "Alberta";
province_list.province_subjects = Object.keys(edu_data["Education_data"].Alberta);
province_list.province_subject_number = Object.values(edu_data["Education_data"].Alberta);

function compile_country_data(){
    var all_country_data = Object.values(edu_data["Education_data"]);
    var complied_data = {
            "NC": 0,
            "HSDO": 0,
            "NATC": 0,
            "AC": 0,
            "PO3": 0,
            "PO1": 0,
            "POM": 0,
            "UBCOD": 0,
            "BD": 0,
            "UACOD": 0,
            "DIMD": 0,
            "MD": 0,
            "ED": 0,
            "NAV": 0,
            "NAP": 0
    };
    // looping through each element Object
    for (let i = 0; i < all_country_data.length; i++){
        var temp_array_keys = Object.keys(all_country_data[i]);
        for (let j = 0; j < temp_array_keys.length; j++){
            complied_data[temp_array_keys[j]] += all_country_data[i][temp_array_keys[j]]
        }
    }
    return complied_data;
}

//getting the province and education selection from the website
let province_choosen = document.getElementById("Province");
let education_choosen = document.getElementById("Education");

const ctx = document.getElementById("myChart");

var BarGraph = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: province_list.province_subjects,
        datasets: [{
            label: "Alberta Educational Attainment #",
            data: province_list.province_subject_number,
            borderWidth: 1
        }]
    },
    optons: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

province_choosen.onclick = function (){
    if (province_choosen.value == "Alberta"){
        // updating the province list accordingly
        province_list.province_name = "Alberta";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Alberta"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Alberta"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Alberta Educational Attainment #";

    } else if (province_choosen.value == "New Brunswick"){
        // updating the province list accordingly
        province_list.province_name = "New Brunswick";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["New Brunswick"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["New Brunswick"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "New Brunswick Educational Attainment #";

    } else if (province_choosen.value == "British Columbia"){
        // updating the province list accordingly
        province_list.province_name = "British Columbia";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["British Columbia"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["British Columbia"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "British Columbia Educational Attainment #";

    } else if (province_choosen.value == "Saskatchewan"){
        // updating the province list accordingly
        province_list.province_name = "Saskatchewan";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Saskatchewan"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Saskatchewan"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Saskatchewan Educational Attainment #";

    } else if (province_choosen.value == "Manitoba"){
        // updating the province list accordingly
        province_list.province_name = "Manitoba";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Manitoba"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Manitoba"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Manitoba Educational Attainment #";

    } else if (province_choosen.value == "Quebec"){
        // updating the province list accordingly
        province_list.province_name = "Quebec";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Quebec"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Quebec"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Quebec Educational Attainment #";

    } else if (province_choosen.value == "Ontario"){
        // updating the province list accordingly
        province_list.province_name = "Ontario";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Ontario"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Ontario"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Ontario Educational Attainment #";

    } else if (province_choosen.value == "Prince Edward Island"){
        // updating the province list accordingly
        province_list.province_name = "Prince Edward Island";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Prince Edward Island"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Prince Edward Island"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Prince Edward Island Educational Attainment #";

    } else if (province_choosen.value == "Newfoundland and Labrador"){
        // updating the province list accordingly
        province_list.province_name = "Newfoundland and Labrador";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Newfoundland and Labrador"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Newfoundland and Labrador"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Newfoundland and Labrador Educational Attainment #";

    } else if (province_choosen.value == "Northern Canada"){
        // updating the province list accordingly
        province_list.province_name = "Northern Canada";
        province_list.province_subjects = Object.keys(edu_data["Education_data"]["Northern Canada"]);
        province_list.province_subject_number = Object.values(edu_data["Education_data"]["Northern Canada"]);
        // updating the bar graph title
        BarGraph.data.datasets[0].label = "Northern Canada Educational Attainment #";

    } else if (province_choosen.value == "All"){
        // compile the data from all province
        var temp_country_data = compile_country_data();
        // sending it ot the object
        province_list.province_name = "All"
        province_list.province_subjects = Object.keys(temp_country_data);
        province_list.province_subject_number = Object.values(temp_country_data);
        // updating the Bar graph title
        BarGraph.data.datasets[0].label = "Country Wide Educational Attainmnet #"
    }
    BarGraph.data.labels = province_list.province_subjects;
    BarGraph.data.datasets[0].data = province_list.province_subject_number;
    BarGraph.update();
}

function find_element_index(some_array, element){
    for (let i = 0; i < some_array.length; i++){
        if (element == some_array[i]){
            return i;
        }
    }
    return -1;
}

var notification = document.getElementById("Notify");

education_choosen.onclick = function (){
    if (education_choosen.value == "No Certificate"){
        var index = find_element_index(province_list.province_subjects, "NC");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["No Certificate"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "No Certificate";

    } else if (education_choosen.value == "Not Available"){
        var index = find_element_index(province_list.province_subjects, "NAV");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Not Available"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Not Available";

    } else if (education_choosen.value == "Not Applicable"){
        var index = find_element_index(province_list.province_subjects, "NAP");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Not Applicable"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Not Applicable";

    } else if (education_choosen.value == "High (secondary) school diploma or equivalency certificate"){
        var index = find_element_index(province_list.province_subjects, "HSDO");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["High (secondary) school diploma or equivalency certificate"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "High (secondary) school diploma or equivalency certificate";

    } else if (education_choosen.value == "Non-apprenticeship trades certificate or diploma"){
        var index = find_element_index(province_list.province_subjects, "NATC");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Non-apprenticeship trades certificate or diploma"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Non-apprenticeship trades certificate or diploma";

    } else if (education_choosen.value == "Apprenticeship Certificate"){
        var index = find_element_index(province_list.province_subjects, "AC");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Apprenticeship Certificate"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Apprenticeship Certificate";

    } else if (education_choosen.value == "Program of 3 months to less than 1 year"){
        var index = find_element_index(province_list.province_subjects, "PO3");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Program of 3 months to less than 1 year"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Program of 3 months to less than 1 year";

    } else if (education_choosen.value == "Program of 1 to 2 years"){
        var index = find_element_index(province_list.province_subjects, "PO1");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Program of 1 to 2 years"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Program of 1 to 2 years";

    } else if (education_choosen.value == "Program of more than 2 years"){
        var index = find_element_index(province_list.province_subjects, "POM");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Program of more than 2 years"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Program of more than 2 years";

    } else if (education_choosen.value == "University certificate or diploma below bachelor level"){
        var index = find_element_index(province_list.province_subjects, "UBCOD");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["University certificate or diploma below bachelor level"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "University certificate or diploma below bachelor level";

    } else if (education_choosen.value == "University certificate or diploma above bachelor level"){
        var index = find_element_index(province_list.province_subjects, "UACOD");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["University certificate or diploma above bachelor level"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "University certificate or diploma above bachelor level";

    } else if (education_choosen.value == "Bachelor's Degree"){
        var index = find_element_index(province_list.province_subjects, "BD");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Bachelor's Degree"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Bachelor's Degree";

    } else if (education_choosen.value == "Degree in medicine, dentistry, veterinary medicine or optometry"){
        var index = find_element_index(province_list.province_subjects, "DIMD");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Degree in medicine, dentistry, veterinary medicine or optometry"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Degree in medicine, dentistry, veterinary medicine or optometry";

    } else if (education_choosen.value == "Master's degree"){
        var index = find_element_index(province_list.province_subjects, "MD");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Master's degree"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Master's degree";

    } else if (education_choosen.value == "Earned doctorate"){
        var index = find_element_index(province_list.province_subjects, "ED");
        if (index == -1){
            notification.textContent = `${education_choosen.value} could not be found in ${province_choosen.value}`;
            return;
        }
        notification.textContent = ""
        BarGraph.data.labels = ["Earned docutorate"];
        BarGraph.data.datasets[0].data = [province_list.province_subject_number[index]];
        BarGraph.data.datasets[0].label = "Earned doctorate";

    }
    BarGraph.update();
}

