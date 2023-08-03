import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
function NavBar() {
  return (
    <>
      <Navbar bg="light" data-bs-theme="light">
      <Container>
          <Navbar.Brand as={Link} to="/Profile">Home</Navbar.Brand> 
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/syllabus">Syllabus</Nav.Link> 
            <Nav.Link as={Link} to="/assignments">Assignments</Nav.Link> 
            <Nav.Link as={Link} to="/resources">Resources</Nav.Link> 
          </Nav>
        </Container>
      </Navbar>
    </>
  );
}

export default NavBar;