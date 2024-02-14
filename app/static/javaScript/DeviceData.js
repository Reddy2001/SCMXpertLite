// Code for displaying active links
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item => {
  const li = item.parentElement;

  item.addEventListener('click', function () {
    allSideMenu.forEach(i => {
      i.parentElement.classList.remove('active');
    })
    li.classList.add('active');
  })
});




// TOGGLE SIDEBAR --> to display the sidebar after clicking the menu icon 
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
  sidebar.classList.toggle('hide');
})


// pagination //


const rowsPerPage = 10; // number of rows per page
const tableBody = document.querySelector('tbody');
const paginationLinks = document.querySelector('.pagination');

// creating an array of all rows in the table body
const tableRows = Array.from(tableBody.querySelectorAll('tr'));

// calculating the total number of pages
const totalPages = Math.ceil(tableRows.length / rowsPerPage);

// display the first page and create pagination links
let currentPage = 1;
displayPage(currentPage);
createPaginationLinks();

function displayPage(pageNumber) {
  // calculate the starting and ending indexes of the rows to display on the given page
  const startIndex = (pageNumber - 1) * rowsPerPage;
  const endIndex = startIndex + rowsPerPage;

  // hide all rows in the table body
  tableRows.forEach(row => row.style.display = 'none');

  // update current page
  currentPage = pageNumber;

  // display the rows for the given page
  for (let i = startIndex; i < endIndex && i < tableRows.length; i++) {
    tableRows[i].style.display = 'table-row';
  }

  // update the page numbers text
  const pageNumbers = document.querySelector('#pageText');
  pageNumbers.textContent = `Showing ${currentPage} of ${totalPages}`;
}

function createPaginationLinks() {
  // create a link for each page and add it to the pagination container
  for (let i = 1; i <= totalPages; i++) {
    const link = document.createElement('a');
    link.href = '#';
    link.textContent = i;
    link.classList.add('page-link');
    link.dataset.pageNumber = i;

    // add an event listener to each link to display the corresponding page when clicked
    link.addEventListener('click', () => {
      const pageNumber = parseInt(link.dataset.pageNumber);
      displayPage(pageNumber);
    });

    paginationLinks.querySelector('ul').appendChild(document.createElement('li')).appendChild(link);
  }
}

function prevPage() {
  if (currentPage > 1) {
    displayPage(currentPage - 1);
  }
}

function nextPage() {
  if (currentPage < totalPages) {
    displayPage(currentPage + 1);
  }
}
