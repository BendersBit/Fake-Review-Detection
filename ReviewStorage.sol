// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReviewStorage {
    struct Review {
        uint id;
        string text;
        bool isFake;
    }

    Review[] public reviews;

    function addReview(uint _id, string memory _text, bool _isFake) public {
        reviews.push(Review(_id, _text, _isFake));
    }

    function getReview(uint index) public view returns (uint, string memory, bool) {
        Review memory r = reviews[index];
        return (r.id, r.text, r.isFake);
    }

    function getTotalReviews() public view returns (uint) {
        return reviews.length;
    }
}
