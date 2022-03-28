export default {
    post: jest.fn(() => Promise.resolve({ data: {} }) ),
    then: jest.fn(() => Promise.resolve())
};