


function searchOrder() {
    // Perform API call to fetch order details based on the entered Order ID
    // Fill the table body with the fetched data
    document.getElementById('orderDetailsTable').classList.remove('hide');
    document.getElementById('orderDetailsTable').classList.add('fadeIn');
}

// document.getElementById('updatebtn').addEventListener('click', function () {
//     // Autofill form fields with the selected order details from the table
//     // Assuming you have a button with an ID 'getVendorButton' in your HTML

//     // Define the URL for the API endpoint
//     var code = document.getElementById("vendor_code").value


//     var xhr = new XMLHttpRequest();
//     xhr.open('GET', `http://127.0.0.1:8000/vendor-dtl/api/getVendor/${code}/`, true);
//     xhr.onreadystatechange = function () {
//         if (xhr.readyState === XMLHttpRequest.DONE) {
//             if (xhr.status === 200) {
//                 var data = JSON.parse(xhr.responseText);
//                 // Process the retrieved data here
//                 console.log(data);
//             } else {
//                 console.error('There was a problem with the request.');
//             }
//         }
//     };
//     xhr.send();



//     document.getElementById('updateForm').classList.remove('hide');
//     document.getElementById('updateForm').classList.add('fadeIn');
// });

function deleteOrder() {
    // Perform deletion of the selected order
    // Handle confirmation/alert before deletion
}

function updateOrder() {
    // Perform update operation with the modified data from the form
    // Show success message or handle errors
}
function openAddVendorDialog() {

    $('#addVendorModal').modal('show');
}
const addVendorModal = new bootstrap.Modal(document.getElementById('addVendorModal'), {
    backdrop: 'static',
    keyboard: false
});

function closeModal() {
    // Close modal
    this.hide();
}

function openSearchDialog() {
    $('#searchModal').modal('show');
}


function openEditVendor(vendorid){

    console.log("-----------------------------called");
    $('#editModal').modal('show');

    console.log(vendorid);

}


const searchModal = new bootstrap.Modal(document.getElementById('searchModal'), {
    backdrop: 'static',
    keyboard: false
});
// Open details modal on Details button click
// $('.editBtn').click(function () {
//     $('#editModal').modal('show');
// });


const editModal = new bootstrap.Modal(document.getElementById('editModal'), {
    backdrop: 'static',
    keyboard: false
});

// Open details modal on Details button click
// $('.detailsBtn').click(function() {
//$('#detailsModal').modal('show');
//}); 

const details = new bootstrap.Modal(document.getElementById('detailsModal'), {
    backdrop: 'static',
    keyboard: false
});



function searchUser() {


    var code = document.getElementById("orderIdInput").value


    var xhr = new XMLHttpRequest();
    xhr.open('GET', `http://127.0.0.1:8000/vendor-dtl/api/getVendor/${code}/`, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);

                console.log(data);




                const table = ` <table class="table table-hover">
        <thead>
            <tr>
                <th scope="col">Vendor Code</th>
                <th scope="col">Vendor Name</th>
                <th scope="col">Edit List </th>
                <th scope="col">List Info</th>
            </tr>
        </thead>
        <tbody>

            <tr>
                <th scope="row">${data.vendor_code}</th>
                <td>${data.name}</td>
                <td>
                      
                        <button id="updatebtn" value="${data.vendor_code}"  onclick="openEditVendor('${data.vendor_code}')"
                            class="btn btn-sm btn-primary editBtn"><i
                                class="far fa-edit"  ></i>
                            edit</button>
                

                   
                        <button value="${data.vendor_code}" id="deletebtn"
                            class="btn btn-sm btn-danger deleteBtn"><i
                                class="fas fa-trash-alt"></i>
                            delete</button>
                    </form>
                </td>
                <td>
                
                        <button  value="${data.vendor_code}" id ="detailsbtn"
                            class="btn btn-sm btn-info detailsBtn"><i
                                class="fas fa-info-circle"></i>
                            Details</button>
                
                </td>
            </tr>

        
        </tbody>
    </table>`
                var myDiv = document.getElementById('myDiv');
                myDiv.insertAdjacentHTML('afterend', table);
            } else {
                console.error('There was a problem with the request.');
            }
        }
    };
    xhr.send();
}
