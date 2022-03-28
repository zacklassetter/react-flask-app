import { render, screen, fireEvent, waitForElement } from '@testing-library/react';
import App from './App';

import axiosMock from "axios";

jest.mock("axios", () => ({
  ...jest.requireActual("axios"),
  post: jest.fn()
}))

it('Async axios request works', async () => {
  axiosMock.post.mockResolvedValue({data: { title: 'some title' } })

  const url = 'https://jsonplaceholder.typicode.com/posts/1'
  const { getByText, getByTestId, rerender } = render(<App />);

  expect(getByTestId("phrase-component").textContent).toBe("")

  const resolvedEl = await waitForElement(() => getByTestId("phrase-component"));

  expect((resolvedEl).textContent).toBe("some title")

  expect(axiosMock.get).toHaveBeenCalledTimes(1);
  expect(axiosMock.get).toHaveBeenCalledWith("/create_phrase");
 })

// test("good response", () => {
//   axios.post.mockResolvedValue({ phrase: 'Ackzay\'s zip code is invalid' });
//   const linkElement = screen.findByTestId("phrase_component");
//   const aboutAnchorNode = screen.getByText('Ackza', {exact: false})
//   print(aboutAnchorNode.value)
//   expect(linkElement.value).toBe('Ackzay\'s zip code is invalid')

// });

// const setup = () => {
//   const utils = render(<App />)
//   const input = utils.getByLabelText('name-input')
//   return input
// }

// test("bad response", () => {
//   //axios.get.mockImplementation(() => Promise.reject({ phrase: "goodbye" }));
//   const input = setup()
//     /* fire events that update state */
  
//   fireEvent.change(input, {target: {value: '23'}})

//   //expect(input.value).toBe('$23')
//   // ...
// });


// test('It should keep a $ in front of the input', async () => {
//   const {input} = setup()
//   fireEvent.change(input, {target: {value: 'zack'}})
//   expect(input.value).toBe('Ackzay\'s zip code is invalid')
// })

test('renders learn react link', async () => {
  render(<App />);
  const linkElement = screen.findByTestId("phrase_component");
  expect(linkElement.value).toBe('Ackzay\'s zip code is invalid')
});
