const User = require("../model/userModel");

exports.getUser = async (req, res) => {
    const user = await User.findById(req.user);

    res.status(200).json({
        name: user.name,
        email: user.email,
        username: user.username,
        id: user._id
    });
};
